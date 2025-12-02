# Krishi Mitra AI: Smart Agriculture Assistant 🌾🚜

[cite_start]**Team:** Data Catalyst [cite: 3]  
[cite_start]**Event:** Innoverse 2025 [cite: 1]

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Status](https://img.shields.io/badge/Status-Prototype-yellow)

## 📖 Introduction
**Krishi Mitra AI** is a comprehensive solution designed to empower small farmers in Karnataka. [cite_start]It addresses critical challenges such as identifying crop diseases, accessing real-time market prices, and understanding government schemes[cite: 10].

[cite_start]By leveraging Artificial Intelligence and Machine Learning, this project bridges the gap between technology and traditional farming, offering an easy-to-use tool in local languages (Kannada/English)[cite: 11].

## 🚀 Key Features

### 1. AI-Driven Disease Detection 🍃
- Uses a **Convolutional Neural Network (CNN)** based on **MobileNetV2** architecture.
- Detects **9 specific classes** of tomato diseases and healthy states, including:
  - Bacterial Spot, Early/Late Blight, Leaf Mold
  - Septoria Leaf Spot, Target Spot
  - Tomato Mosaic Virus, Yellow Leaf Curl Virus
  - Spider Mites
- Provides detailed treatment recommendations (Chemical & Organic) and prevention methods.

### 2. Digital Agriculture Adoption 📱
- [cite_start]**Real-time Market Prices:** Fetches mandi data to keep farmers informed[cite: 20].
- [cite_start]**Government Schemes:** An NLP-based chatbot explains subsidies and schemes in local languages[cite: 23].

### 3. Accessibility 🗣️
- [cite_start]**Multilingual Support:** Designed with a Kannada UI and voice chatbot capabilities for rural accessibility[cite: 27, 37].

## 🛠️ Tech Stack

* [cite_start]**Backend:** Python, FastAPI [cite: 55]
* [cite_start]**Machine Learning:** TensorFlow, Keras, NumPy [cite: 56]
* **Image Processing:** Pillow (PIL)
* **Architecture:** MobileNetV2 (Transfer Learning)

## 📂 Project Structure

```text
├── dataset/               # Training images organized by class
├── models/                # Saved models (.h5) and class indices (.json)
├── app.py                 # Main FastAPI application
├── disease_info.py        # Database of disease treatments and prevention
├── train.py               # Model training script
├── train_quick.py         # Balanced training script with class weights
├── test_api.py            # Script to test API endpoints
└── requirements.txt       # Project dependencies
