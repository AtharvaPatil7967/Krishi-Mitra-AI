# check_dataset.py
import os

dataset_path = "dataset"
print("="*60)
print("DATASET DISTRIBUTION")
print("="*60)

total = 0
for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    if os.path.isdir(folder_path):
        count = len([f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
        total += count
        print(f"{folder:30} : {count:5} images")

print("="*60)
print(f"TOTAL: {total} images")
