# Tomato Disease Detection API - Complete Documentation

## ✅ Model Performance
- **Training Accuracy:** 82.10%
- **Validation Accuracy:** 88.49%
- **Test Accuracy:** 90% (9/10 correct)
- **Model Size:** 16 MB

## 🚀 API Endpoints

### 1. GET /
Basic API information

### 2. GET /health
Health check for monitoring

### 3. GET /classes
List all 10 disease classes

### 4. POST /predict
**Main endpoint - Upload image and get prediction**

## 📤 Request Format

**Endpoint:** `POST http://localhost:8001/predict`
**Content-Type:** `multipart/form-data`
**Field name:** `file` (must be exactly "file")

### Example with JavaScript:
