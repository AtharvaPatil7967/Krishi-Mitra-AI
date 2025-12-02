# test_api.py
import requests
import json

API_URL = "http://localhost:8000/predict"

def test_prediction(image_path):
    """Test the API with an image"""
    print(f"\nTesting with: {image_path}")
    print("-" * 50)
    
    try:
        with open(image_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(API_URL, files=files)
            
        result = response.json()
        print(json.dumps(result, indent=2))
        
    except FileNotFoundError:
        print(f"ERROR: Image file '{image_path}' not found!")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    print("="*60)
    print("TESTING TOMATO DISEASE DETECTION API")
    print("="*60)
    
    # Test with your images
    test_prediction("test_tomato_healthy.jpg")
    test_prediction("test_tomato_disease.jpg")
    
    print("\n" + "="*60)
