import torch
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
from torch import nn, optim

# Image preparation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Load dataset
train_data = datasets.ImageFolder("dataset/train", transform=transform)
val_data = datasets.ImageFolder("dataset/validation", transform=transform)

train_loader = DataLoader(train_data, batch_size=4, shuffle=True)
val_loader = DataLoader(val_data, batch_size=4)

# Load pre-trained MobileNetV3
model = models.mobilenet_v3_small(weights="DEFAULT")

# Freeze the existing model
for parameter in model.parameters():
    parameter.requires_grad = False

# Change final layer for our 2 classes
model.classifier[3] = nn.Linear(
    model.classifier[3].in_features,
    2
)

# Loss and optimizer
loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.classifier[3].parameters(), lr=0.001)

# Training
for epoch in range(5):

    model.train()

    for images, labels in train_loader:

        optimizer.zero_grad()

        outputs = model(images)

        loss = loss_function(outputs, labels)

        loss.backward()

        optimizer.step()

    # Validation
    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in val_loader:

            outputs = model(images)
            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total

    print(
        f"Epoch {epoch + 1}/5 "
        f"- Validation Accuracy: {accuracy:.2f}%"
    )

# Save model
torch.save(model.state_dict(), "model/ai_art_detector.pth")

print("Training completed!")
print("Model saved successfully.")