# train_quick.py - BALANCED TRAINING
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.utils import class_weight
import numpy as np
import json
import os

DATASET_PATH = 'dataset'
IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 10  # Quick training

print("="*60)
print("QUICK BALANCED TRAINING")
print("="*60)

# Data with augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    horizontal_flip=True,
    validation_split=0.2
)

# Load data
train_gen = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

val_gen = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation',
    shuffle=False
)

# Calculate class weights to handle imbalance
class_weights = class_weight.compute_class_weight(
    'balanced',
    classes=np.unique(train_gen.classes),
    y=train_gen.classes
)
class_weight_dict = dict(enumerate(class_weights))

print(f"\nClass weights (to balance dataset):")
for idx, weight in class_weight_dict.items():
    class_name = list(train_gen.class_indices.keys())[idx]
    print(f"  {class_name}: {weight:.2f}")

# Save class names
class_names = {v: k for k, v in train_gen.class_indices.items()}
os.makedirs('models', exist_ok=True)
with open('models/class_names.json', 'w') as f:
    json.dump(class_names, f, indent=2)

# Build model
base_model = MobileNetV2(
    input_shape=(IMG_SIZE, IMG_SIZE, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.5),  # Higher dropout
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(len(class_names), activation='softmax')
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\nTraining with class balancing...")
print("="*60)

# Train with class weights
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS,
    class_weight=class_weight_dict,  # THIS FIXES IMBALANCE!
    callbacks=[
        tf.keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(patience=2)
    ]
)

# Save
model.save('models/tomato_model.h5')
print("\n✓ Model saved!")
print(f"Final accuracy: {history.history['val_accuracy'][-1]:.2%}")
