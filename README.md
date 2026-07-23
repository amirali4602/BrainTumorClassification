# 🧠 Brain Tumor MRI Classification

A desktop application for **Brain Tumor MRI Classification** using Deep Learning and TensorFlow. The application allows users to load MRI scans, classify brain tumors using multiple CNN architectures, compare model performance, retrain models, and visualize evaluation metrics through an intuitive PySide6 interface.

---

## ✨ Features

* 🖼️ Load MRI images using file dialog or drag & drop
* 🤖 Predict tumor type using multiple deep learning models
* 📊 Display prediction confidence for every class
* 📈 Visualize model performance metrics
* 🔄 Retrain models directly from the application
* 📉 Automatic confusion matrix generation
* 📝 Training reports and evaluation metrics
* 📂 Model comparison dashboard
* 🖥️ Modern desktop interface built with PySide6

---

## 🧠 Supported Classes

The models classify MRI images into four categories:

* Glioma
* Meningioma
* No Tumor
* Pituitary Tumor

---

## 🤖 Implemented Models

The project currently includes the following neural network architectures:

| Model             | Type                |
| ----------------- | ------------------- |
| Custom CNN        | Custom Architecture |
| ResNet50          | Transfer Learning   |
| EfficientNetB0    | Transfer Learning   |
| DenseNet121       | Transfer Learning   |
| EfficientNetV2B0  | Transfer Learning   |
| MobileNetV3 Large | Transfer Learning   |
| Xception          | Transfer Learning   |

Each model can be trained, evaluated, and compared independently.

---

## 🖥️ Application Overview

### Prediction

* Load MRI image
* Select trained model
* Predict tumor type
* Display confidence scores
* Probability distribution for every class

### Analytics

* Accuracy comparison
* Precision comparison
* Recall comparison
* F1-score comparison
* Confusion matrix comparison
* Training curves
* Classification reports

### Retraining

The application allows retraining any available model directly from the GUI by selecting:

* Model
* Number of epochs

After training, evaluation reports and comparison charts are automatically regenerated.

---

## 📁 Dataset Structure

```text
dataset/
│
├── Training/
│   ├── glioma/
│   ├── meningioma/
│   ├── notumor/
│   └── pituitary/
│
└── Testing/
    ├── glioma/
    ├── meningioma/
    ├── notumor/
    └── pituitary/
```

---

## 📂 Project Structure

```text
Brain-Tumor-MRI-Classification
│
├── app/
│   ├── evaluation/
│   ├── gui/
│   ├── inference/
│   ├── models/
│   ├── preprocessing/
│   ├── training/
│   └── utils/
│
├── dataset/
├── saved_models/
├── results/
├── reports/
├── logs/
├── main.py
└── requirements.txt
```

---

## ⚙️ Technologies

* Python
* TensorFlow / Keras
* PySide6
* NumPy
* Matplotlib
* scikit-learn

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Brain-Tumor-MRI-Classification.git
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

## 🏋️ Training

Models can be trained either:

### From the GUI

Toolbar → **Retrain Model**

or

### From Python

```bash
python train.py
```

Training automatically saves:

* Best model
* Training history
* Accuracy/Loss curves
* Evaluation metrics
* Classification report
* Confusion matrix
* Predictions
* Comparison charts

---

## 📊 Evaluation Metrics

Every trained model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report

Comparison charts are generated automatically after training.

---

## 📸 Screenshots

### Prediction

> Add a screenshot of the prediction interface here.

### Analytics

> Add a screenshot of the analytics dashboard here.

### Model Comparison

> Add the generated comparison charts here.

---

## 📹 Demo Video



---
## 📈 Future Improvements

* Vision Transformer (ViT)
* ConvNeXt
* Grad-CAM visualization
* Ensemble predictions
* Model explainability
* Test-time augmentation
* Mixed precision training
* ONNX export
* GPU benchmark comparison

---

## 📜 License

This project is intended for educational and research purposes.

---

## 👨‍💻 Author

AmirAli Mehdipour
Developed as a Deep Learning and Medical Image Classification project using TensorFlow and PySide6.
