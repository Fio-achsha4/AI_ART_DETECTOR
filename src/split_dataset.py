import os
import shutil
import random

random.seed(42)

classes = ["ai", "human"]

for class_name in classes:
    source = f"dataset/{class_name}"

    images = [
        file for file in os.listdir(source)
        if file.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    random.shuffle(images)

    total = len(images)

    train_end = int(total * 0.7)
    val_end = int(total * 0.85)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    for folder, image_list in [
        ("train", train_images),
        ("validation", val_images),
        ("test", test_images)
    ]:
        destination = f"dataset/{folder}/{class_name}"
        os.makedirs(destination, exist_ok=True)

        for image in image_list:
            shutil.copy(
                os.path.join(source, image),
                os.path.join(destination, image)
            )

    print(f"{class_name}: {len(train_images)} train, "
          f"{len(val_images)} validation, {len(test_images)} test")

print("Dataset splitting completed!")