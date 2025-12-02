# train.py
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import json
import os

# Configuration
DATASET_PATH = 'dataset'  # Your 12000 images folder
IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 15  # Can increase for better accuracy

print("=" * 50)
print("TOMATO DISEASE DETECTION - MODEL TRAINING")
print("=" * 50)

# Check if dataset exists
if not os.path.exists(DATASET_PATH):
    print(f"ERROR: Dataset folder '{DATASET_PATH}' not found!")
    print("Please create the dataset folder and organize images by disease class.")
    exit(1)

# Data Augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest',
    validation_split=0.2  # 80% train, 20% validation
)

# Training data
print("\nLoading training data...")
train_generator = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

# Validation data
print("Loading validation data...")
validation_generator = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation',
    shuffle=False
)

# Save class names
class_indices = train_generator.class_indices
class_names = {v: k for k, v in class_indices.items()}

os.makedirs('models', exist_ok=True)
with open('models/class_names.json', 'w') as f:
    json.dump(class_names, f, indent=2)

print(f"\n✓ Found {len(class_names)} disease classes:")
for idx, name in class_names.items():
    print(f"  {idx}: {name}")

print(f"\n✓ Training samples: {train_generator.samples}")
print(f"✓ Validation samples: {validation_generator.samples}")

# Build model with Transfer Learning
print("\nBuilding model with MobileNetV2...")
base_model = MobileNetV2(
    input_shape=(IMG_SIZE, IMG_SIZE, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.3),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(len(class_names), activation='softmax')
])

# Compile
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\n" + "=" * 50)
model.summary()
print("=" * 50)

# Callbacks
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    ),
    tf.keras.callbacks.ModelCheckpoint(
        'models/best_model.h5',
        monitor='val_accuracy',
        save_best_only=True,
        verbose=1
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=3,
        verbose=1
    )
]

# Train
print("\nStarting training...")
print("=" * 50)

history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=EPOCHS,
    callbacks=callbacks,
    verbose=1
)

# Save final model
model.save('models/tomato_model.h5')

print("\n" + "=" * 50)
print("TRAINING COMPLETE!")
print("=" * 50)
print(f"✓ Model saved to: models/tomato_model.h5")
print(f"✓ Best model saved to: models/best_model.h5")
print(f"✓ Class names saved to: models/class_names.json")
print(f"✓ Final training accuracy: {history.history['accuracy'][-1]:.2%}")
print(f"✓ Final validation accuracy: {history.history['val_accuracy'][-1]:.2%}")
print("=" * 50)
