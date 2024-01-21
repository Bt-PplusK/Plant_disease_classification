import cv2
import numpy as np
import torch

# Load and preprocess the new image
image_path = "/content/images (8).jpg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # If your model expects RGB
image = cv2.resize(image, (256, 256))  # Adjust the size as needed
image = image / 255.0  # Normalize the pixel values

# Load the model
model = torch.load('/content/densenet121_model.pt', map_location=torch.device('cpu'))
model.eval()
# Convert the image to a PyTorch tensor
image_tensor = torch.tensor(image.transpose(2, 0, 1), dtype=torch.float32)

# Add batch dimension (if needed)
image_tensor = image_tensor.unsqueeze(0)

# Make the prediction
with torch.no_grad():
    output = model(image_tensor)

# Convert the output to probabilities using softmax
probabilities = torch.nn.functional.softmax(output[0], dim=0)

# Get the predicted class index
predicted_class = torch.argmax(probabilities).item()

print("Raw Output Probabilities:", output[0].tolist())
print("Predicted Class Index:", predicted_class)
class_index_to_label = {0: 'Healthy', 1: 'Powdery',2: 'Rust'}
predicted_label = class_index_to_label[predicted_class]
print(f"Predicted Label: {predicted_label}")