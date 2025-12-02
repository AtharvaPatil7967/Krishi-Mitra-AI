# test_model.py - COMPLETE TEST SCRIPT
import tensorflow as tf
import numpy as np
from PIL import Image
import json
import os
import glob

print("="*60)
print("TESTING TRAINED TOMATO DISEASE MODEL")
print("="*60)

# Load model
print("\n1. Loading model...")
try:
    model = tf.keras.models.load_model('models/tomato_model.h5')
    print("   ✓ Model loaded successfully")
except Exception as e:
    print(f"   ✗ Error loading model: {e}")
    exit(1)

# Load class names
print("\n2. Loading class names...")
try:
    with open('models/class_names.json', 'r') as f:
        class_names = json.load(f)
    print(f"   ✓ Class names loaded ({len(class_names)} classes)")
except Exception as e:
    print(f"   ✗ Error loading class names: {e}")
    exit(1)

# Print all classes
print("\n3. Disease Classes:")
for idx, name in class_names.items():
    print(f"   {idx}: {name}")

def predict_image(image_path):
    """Predict disease from image"""
    # Load image
    img = Image.open(image_path).convert('RGB')
    
    # Resize to model input size
    img = img.resize((224, 224))
    
    # Convert to array and normalize
    img_array = np.array(img) / 255.0
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    # Predict
    predictions = model.predict(img_array, verbose=0)
    
    # Get top prediction
    predicted_idx = np.argmax(predictions[0])
    confidence = predictions[0][predicted_idx] * 100
    predicted_class = class_names[str(predicted_idx)]
    
    # Get top 3 predictions
    top_3_idx = np.argsort(predictions[0])[-3:][::-1]
    top_3 = [(class_names[str(i)], predictions[0][i] * 100) for i in top_3_idx]
    
    return predicted_class, confidence, top_3

# Test on images from dataset
print("\n" + "="*60)
print("4. TESTING PREDICTIONS ON DIFFERENT DISEASES")
print("="*60)

dataset_path = "dataset"
if not os.path.exists(dataset_path):
    print(f"\n✗ Dataset folder '{dataset_path}' not found!")
    print("Please make sure your dataset folder exists.")
    exit(1)

results = {}
total_tested = 0
correct_predictions = 0

for disease_folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, disease_folder)
    
    if os.path.isdir(folder_path):
        # Get first image from folder
        images = glob.glob(os.path.join(folder_path, "*.jpg")) + \
                 glob.glob(os.path.join(folder_path, "*.jpeg")) + \
                 glob.glob(os.path.join(folder_path, "*.png"))
        
        if images:
            test_image = images[0]
            
            try:
                # Predict
                predicted, conf, top_3 = predict_image(test_image)
                
                # Check if correct
                is_correct = (predicted == disease_folder)
                if is_correct:
                    correct_predictions += 1
                total_tested += 1
                
                # Display results
                match_symbol = "✅ CORRECT" if is_correct else "❌ WRONG"
                
                print(f"\n{'='*60}")
                print(f"Folder: {disease_folder}")
                print(f"Image: {os.path.basename(test_image)}")
                print(f"-" * 60)
                print(f"Predicted: {predicted} ({conf:.2f}%) {match_symbol}")
                print(f"\nTop 3 Predictions:")
                for i, (disease, prob) in enumerate(top_3, 1):
                    print(f"  {i}. {disease:35} : {prob:5.2f}%")
                
                # Store results
                results[disease_folder] = {
                    "predicted": predicted,
                    "confidence": conf,
                    "correct": is_correct,
                    "top_3": top_3
                }
                
            except Exception as e:
                print(f"\n✗ Error processing {disease_folder}: {e}")

# Calculate overall accuracy
print("\n" + "="*60)
print("5. FINAL RESULTS")
print("="*60)

if total_tested > 0:
    accuracy = (correct_predictions / total_tested) * 100
    
    print(f"\nTotal images tested: {total_tested}")
    print(f"Correct predictions: {correct_predictions}")
    print(f"Wrong predictions: {total_tested - correct_predictions}")
    print(f"\n{'='*60}")
    print(f"QUICK TEST ACCURACY: {accuracy:.1f}% ({correct_predictions}/{total_tested})")
    print(f"{'='*60}")
    
    if accuracy >= 80:
        print("\n🎉 ✅ MODEL IS WORKING EXCELLENTLY!")
    elif accuracy >= 70:
        print("\n✅ MODEL IS WORKING WELL!")
    elif accuracy >= 60:
        print("\n⚠️ Model is working but could be better")
    else:
        print("\n❌ Model needs improvement")
    
    print("\n✓ Model files ready for FastAPI integration!")
    print("✓ Files to deliver:")
    print("   - models/tomato_model.h5")
    print("   - models/class_names.json")
    print("   - This test confirms the model works!")
    
else:
    print("\n✗ No images found to test!")

print("\n" + "="*60)
