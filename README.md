# AI Art Detector 🎨🌸

## 1. Project Overview

AI Art Detector is a machine learning tool designed to classify artwork as likely AI-generated or human-created. It provides probability estimates to help users analyze the visual characteristics of artwork.

The project uses a MobileNetV3-Small image classification model trained on AI generated and human created artwork.

## 2. Objectives

- Detect visual patterns in artwork images.
- Classify images into AI and human categories.
- Display prediction probabilities.
- Provide a simple, interactive web interface.
- Connect a machine learning model to a Flask backend.

## 3. Technologies Used

- Python
- PyTorch and Torchvision
- MobileNetV3-Small
- Flask and Flask-CORS
- HTML
- CSS
- JavaScript
- Pillow

## 4. Main Features

- Upload artwork images.
- Preview the selected image.
- Predict AI or human artwork.
- Display AI and human probabilities.
- Show a confidence meter.
- Clear the selection and test another image.

## 5. Project Structure

```text
AI_ART_DETECTOR/
├── app.py
├── model/
│   └── ai_art_detector.pth
├── dataset/
│   ├── ai/
│   ├── human/
│   ├── train/
│   ├── validation/
│   └── test/
├── src/
│   ├── train1.py
│   ├── test1.py
│   ├── predict1.py
│   ├── split_dataset.py
│   └── web/
│       ├── index.html
│       ├── style.css
│       └── script.js
└── test_images/
```

## 6. Installation

Create and activate a Python virtual environment.

Install the required packages:

```bash
pip install torch torchvision flask flask-cors pillow numpy pandas opencv-python matplotlib scikit-learn
```

## 7. Running the Project

Open the project folder in VS Code.

Start the backend from the project root:

```bash
python app.py
```

Open `src/web/index.html` using VS Code Live Server.

Upload an artwork image and click the **Detect Artwork**.

Keep the Flask server running while using the website.

## 8. Model Evaluation

The model was evaluated on a held-out test dataset of 180 images.

**Recorded test accuracy: 78.89%**

This result applies to the test dataset used in this project. Performance on other artwork and unseen image sources may differ.

## 9. Limitations

- Predictions are not proof of an artwork's origin.
- Results depend on the quality and diversity of the training dataset.
- The model may misclassify unfamiliar art styles.
- Prediction probabilities are not guaranteed to represent real-world accuracy.

## 10. Conclusion

The project demonstrates how image classification and web technologies can be combined to build an AI art detection application. It provides an interactive interface for uploading artwork and viewing model predictions.

## 11. Author

Developed as a machine learning and web application project.

### Project Highlights

- Image classification using MobileNetV3-Small
- AI vs Human artwork classification
- Flask REST API
- Interactive HTML/CSS/JavaScript frontend
- Confidence and probability visualization
- Train, validation and test dataset separation
- Model evaluation using a held-out test set
