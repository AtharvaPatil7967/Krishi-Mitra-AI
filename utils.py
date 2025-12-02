# utils.py
import numpy as np
from PIL import Image

def validate_plant_image(image: Image.Image) -> tuple[bool, str]:
    """
    Validate if uploaded image is likely a plant leaf
    Returns: (is_valid, error_message)
    """
    # Check minimum size
    if image.width < 50 or image.height < 50:
        return False, "Image too small. Please upload a clearer image."
    
    # Check aspect ratio
    aspect_ratio = max(image.width, image.height) / min(image.width, image.height)
    if aspect_ratio > 10:
        return False, "Image aspect ratio unusual. Please crop to show only the leaf."
    
    # Color validation - check for greenish tones
    img_array = np.array(image.resize((100, 100)))
    
    if len(img_array.shape) == 3 and img_array.shape[2] >= 3:
        green = img_array[:, :, 1]
        red = img_array[:, :, 0]
        blue = img_array[:, :, 2]
        
        # Count greenish pixels
        green_pixels = np.sum((green > red) & (green > blue))
        total_pixels = img_array.shape[0] * img_array.shape[1]
        green_ratio = green_pixels / total_pixels
        
        # Plants should have at least some green
        if green_ratio < 0.05:
            return False, "Image doesn't appear to be a plant leaf. Please upload a tomato leaf image."
    
    return True, ""

def preprocess_image(image: Image.Image, target_size=(224, 224)) -> np.ndarray:
    """
    Preprocess image for model prediction
    """
    # Resize
    image = image.resize(target_size)
    
    # Convert to array
    img_array = np.array(image)
    
    # Handle different image modes
    if len(img_array.shape) == 2:  # Grayscale
        img_array = np.stack([img_array] * 3, axis=-1)
    elif img_array.shape[2] == 4:  # RGBA
        img_array = img_array[:, :, :3]
    
    # Normalize to [0, 1]
    img_array = img_array.astype('float32') / 255.0
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def get_risk_level(confidence: float, severity: str) -> str:
    """Calculate risk level"""
    if severity == "None":
        return "NONE"
    elif severity == "Very High":
        return "CRITICAL" if confidence > 80 else "HIGH"
    elif severity == "High":
        return "HIGH" if confidence > 75 else "MEDIUM"
    elif severity == "Medium":
        return "MEDIUM" if confidence > 70 else "LOW"
    else:
        return "LOW"
