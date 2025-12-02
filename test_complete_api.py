# test_complete_api.py
import requests
import json

# Test with an image from your dataset
image_path = "dataset/Early_blight/0012b9d2-2130-4a06-a834-b1f3af34f57e___RS_Erly.B 8389.JPG"

print("Testing Complete API with Full JSON Response")
print("="*60)

with open(image_path, 'rb') as f:
    response = requests.post(
        'http://localhost:8001/predict',
        files={'file': f}
    )

result = response.json()

# Pretty print the complete JSON
print(json.dumps(result, indent=2))

print("\n" + "="*60)
print("✓ Complete JSON response received!")
