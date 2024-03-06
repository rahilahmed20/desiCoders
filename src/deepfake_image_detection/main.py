from PIL import Image
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
from io import BytesIO
import requests
import argparse

# Load the pre-trained model and processor
processor = AutoImageProcessor.from_pretrained("dima806/deepfake_vs_real_image_detection")
model = AutoModelForImageClassification.from_pretrained("dima806/deepfake_vs_real_image_detection")

def classify_image_from_url(image_url):
    response = requests.get(image_url)
    image_bytes = response.content

    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    with torch.no_grad():
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        return predicted_class == 0  # Return True if predicted as real, False otherwise


