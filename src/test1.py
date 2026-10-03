import torch
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
from torch import nn

# Prepare images
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Load test dataset
test_data = datasets.ImageFolder(
    "dataset/test",
    transform=transform
)

test_loader = DataLoader(
    test_data,
    batch_size=1,
    shuffle=False
)

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

# Test
correct = 0
total = 0

print("\n--- TEST RESULTS ---")

with torch.no_grad():

    for images, labels in test_loader:

        output = model(images)

        prediction = torch.argmax(output, dim=1)

        actual = labels.item()
        predicted = prediction.item()

        actual_name = test_data.classes[actual]
        predicted_name = test_data.classes[predicted]

        print(
            f"Actual: {actual_name} | "
            f"Predicted: {predicted_name}"
        )

        if actual == predicted:
            correct += 1

        total += 1

accuracy = 100 * correct / total

print("\n--------------------")
print(f"Correct: {correct}/{total}")
print(f"Test Accuracy: {accuracy:.2f}%")
