# app.py - COMPLETE VERSION WITH FULL JSON OUTPUT
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import tensorflow as tf
import numpy as np
import json
import io
from disease_info import DISEASE_DATABASE

# Initialize FastAPI
app = FastAPI(
    title="Tomato Disease Detection API",
    description="ML API for Karnataka Smart Agriculture - Hackathon 2025",
    version="1.0"
)

# CORS - Allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
print("="*60)
print("LOADING TOMATO DISEASE DETECTION MODEL")
print("="*60)
model = tf.keras.models.load_model('models/best_model.h5')
with open('models/class_names.json', 'r') as f:
    class_names = json.load(f)
print(f"✓ Model loaded with {len(class_names)} classes")
print("✓ API Ready!")
print("="*60)

@app.get("/")
def home():
    """API Home - Basic Info"""
    return {
        "message": "Tomato Disease Detection API",
        "status": "Running",
        "version": "1.0",
        "model_accuracy": "88-90%",
        "classes": len(class_names),
        "endpoint": "POST /predict"
    }

@app.get("/health")
def health_check():
    """Health check for deployment"""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "classes_loaded": len(class_names)
    }

@app.get("/classes")
def get_classes():
    """Get all disease classes"""
    return {
        "total_classes": len(class_names),
        "classes": class_names
    }

@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    """
    Main Prediction Endpoint
    Upload tomato leaf image and get complete disease analysis
    """
    try:
        # Read and preprocess image
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data)).convert('RGB')
        
        # Resize to model input size
        image = image.resize((224, 224))
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Predict
        predictions = model.predict(img_array, verbose=0)
        
        # Get top prediction
        predicted_idx = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_idx] * 100)
        predicted_class = class_names[str(predicted_idx)]
        
        # Get top 3 predictions
        top_3_idx = np.argsort(predictions[0])[-3:][::-1]
        top_3_predictions = [
            {
                "disease": class_names[str(i)],
                "confidence": round(float(predictions[0][i] * 100), 2)
            }
            for i in top_3_idx
        ]
        
        # Get complete disease information from database
        disease_data = DISEASE_DATABASE.get(predicted_class, {
            "disease_name": predicted_class,
            "description": "Disease information not available",
            "severity": "Unknown",
            "treatment": {
                "chemical": "Consult agricultural expert",
                "organic": "Maintain plant hygiene",
                "frequency": "As needed"
            },
            "prevention": ["Regular monitoring"],
            "cultural_practices": ["Good sanitation"]
        })
        
        # Calculate risk level
        severity = disease_data.get("severity", "Unknown")
        if severity == "None":
            risk_level = "NONE"
        elif severity == "Very High":
            risk_level = "CRITICAL" if confidence > 80 else "HIGH"
        elif severity == "High":
            risk_level = "HIGH" if confidence > 75 else "MEDIUM"
        elif severity == "Medium":
            risk_level = "MEDIUM" if confidence > 70 else "LOW"
        else:
            risk_level = "LOW"
        
        # Build complete JSON response
        response = {
            "success": True,
            "predicted_class": predicted_class,
            "disease": disease_data["disease_name"],
            "confidence": round(confidence, 2),
            "risk_level": risk_level,
            "description": disease_data["description"],
            "severity": disease_data["severity"],
            "treatment": disease_data["treatment"],
            "prevention": disease_data["prevention"],
            "cultural_practices": disease_data["cultural_practices"],
            "top_3_predictions": top_3_predictions,
            "model_version": "1.0",
            "timestamp": None  # Frontend can add timestamp
        }
        
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*60)
    print("STARTING TOMATO DISEASE DETECTION API SERVER")
    print("="*60)
    print("Server will start on: http://localhost:8001")
    print("Interactive docs: http://localhost:8001/docs")
    print("="*60 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=False)
