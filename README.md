# Plant_disease_classification_with_Pretrained model

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Deployment](#deployment)

## Introduction
This project focuses on the classification of plant health conditions, specifically targeting three categories: Healthy, Powdery Mildew, and Rust. The goal is to develop a robust model that can accurately identify and differentiate between these conditions based on images of plant leaves.

### Background
Agriculture plays a crucial role in sustaining human life, providing food, and supporting economies worldwide. However, the agricultural sector faces numerous challenges, one of which is the impact of plant diseases on crop yield and quality. Diseases like powdery mildew and rust can lead to devastating consequences if not identified and addressed promptly.

### Project Objective
The primary goal of this project is to develop a densenet121 model that can accurately recognize and classify 3 different types of leaves.

### Potential Applications
Precision Agriculture: Optimize resource use through targeted disease information.

Early Warning System: Detect and prevent plant diseases in their early stages.

Crop Monitoring: Continuously monitor crop health for informed decision-making.

Decision Support Tool: Aid agronomists in assessing and managing plant health.

Educational Tool: Educate farmers on common plant diseases and best practices.

Mobile Applications: Enable on-the-spot disease diagnosis using mobile devices.

Automated Farming Systems: Integrate with robotic or drone platforms for autonomous disease identification.

Research and Surveillance: Support plant pathology research and disease surveillance.

Supply Chain Optimization: Ensure delivery of high-quality, disease-free crops, optimizing the supply chain.

Global Food Security: Contribute to global food security by enhancing crop productivity.

Cross-Crop Adaptability: Demonstrate adaptability to various crops and agricultural settings.

Community Engagement: Engage local communities in plant health awareness and sustainable farming.

## Dataset
Firstly,I downloaded dataset from kaggle.The model is trained on a comprehensive dataset that includes images of plant leaves representing various health conditions. The dataset is carefully curated and labeled with three classes: Healthy, Powdery Mildew, and Rust. Each class provides a diverse range of images to ensure the model's generalization across different plant species and environmental conditions.
The dataset is split into three distinct sets for training , validation, and testing.
The dataset is available at Google drive.

### EDA 
An exploratory data analysis (EDA) for this project is provided in the Plant_disease_classification.ipynb notebook. It contains visualizations and insights derived from the dataset.Moreover,it also include augmentation.

## Deployment

### Local Test (Docker Container)

Execute the following command to build the Docker image. This will create an image with the tag ` plant_disease_classification` (you can pick another name if you want).

```bash
$ docker build -t  plant_disease_classification
```

This process might take several minutes as Docker needs to download the base images and build the necessary layers for your application.

Run the following command to start a container based on the image you just created. This command also maps port `8080` of the container to port `8080` on your local machine.

```bash
$ docker run -p 5000:5000 plant_disease_classification
```
