from flask import Flask, request, jsonify
from flask_cors import CORS

import torch
from torchvision import transforms, models
from PIL import Image

from torch import nn


# Create Flask app
app = Flask(__name__)

CORS(app)


# Classes
classes = ["ai", "human"]


# Image preparation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])


# Load model
model = models.mobilenet_v3_small(weights=None)

model.classifier[3] = nn.Linear(
    model.classifier[3].in_features,
    2
)


# Load our trained model
model.load_state_dict(
    torch.load(
        "model/ai_art_detector.pth",
        map_location=torch.device("cpu")
    )
)

model.eval()


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    # Check if image was sent
    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400


    file = request.files["image"]


    # Open image
    image = Image.open(file).convert("RGB")


    # Prepare image
    image = transform(image).unsqueeze(0)


    # Predict
    with torch.no_grad():

        output = model(image)

        probabilities = torch.softmax(
            output,
            dim=1
        )

        confidence, prediction = torch.max(
            probabilities,
            1
        )


    # Get probabilities
    ai_probability = probabilities[0][0].item() * 100

    human_probability = probabilities[0][1].item() * 100


    # Get prediction
    result = classes[prediction.item()]


    return jsonify({

        "prediction": result,

        "ai_probability": round(
            ai_probability, 2
        ),

        "human_probability": round(
            human_probability, 2
        )

    })


# Start server
if __name__ == "__main__":

    print("🌸 AI Art Detector server starting...")

    app.run(
        debug=True,
        port=5000
    )