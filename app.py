from flask import Flask, render_template, request
import torch
from torch import nn
from PIL import Image
from torchvision import transforms
from torchvision import models


app = Flask(__name__)

class PlantDiseaseModel(nn.Module):
    def __init__(self, classes=2):
        super(PlantDiseaseModel, self).__init__()
        self.model = models.densenet121(pretrained=True)
        in_features = self.model.classifier.in_features
        self.model.classifier = nn.Linear(in_features, classes)

    def forward(self, image):
        output = self.model(image)
        return output

model = torch.load('C:\Plant_disease_classification\densenet121_model.pt', map_location=torch.device('cpu'))
model.eval()

# Define image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    try:
        # Open and preprocess the image
        img = Image.open(file).convert('RGB')
        img = transform(img).unsqueeze(0)

        # Perform inference
        with torch.no_grad():
            output = model(img)

        # Extract classification result
        _, predicted = torch.max(output, 1)
        class_label = predicted.item()

        # Map class label to human-readable class name
        classes = ['Healthy', 'Powdery', 'Rust']
        result = classes[class_label]

        return render_template('result.html', result=result)

    except Exception as e:
        return render_template('index.html', error=f'Error processing the file: {e}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
