import torch
from torchvision import transforms, models
from PIL import Image
from torch import nn

# Classes
classes = ["ai", "human"]

# Prepare image
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

model.load_state_dict(
    torch.load("model/ai_art_detector.pth")
)

model.eval()

# Ask for image
image_path = input("Enter image path: ")

image = Image.open(image_path).convert("RGB")

image = transform(image).unsqueeze(0)

# Prediction
with torch.no_grad():

    output = model(image)

    probabilities = torch.softmax(output, dim=1)

    confidence, prediction = torch.max(probabilities, 1)

# Result
ai_probability = probabilities[0][0].item() * 100
human_probability = probabilities[0][1].item() * 100

result = classes[prediction.item()]

print()
print("----------------------------")
print("      AI ART DETECTOR")
print("----------------------------")
print("Prediction:", result)
print(f"AI Probability: {ai_probability:.2f}%")
print(f"Human Probability: {human_probability:.2f}%")
print("----------------------------")