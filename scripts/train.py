from ultralytics import YOLO
import torch

# Load YOLOv11 model
model = YOLO("weights/yolo11n.pt")

# Train the model on your dataset with early stopping
model.train(data="data.yaml", epochs=100, imgsz=480, patience=10)

# Save trained weights
model.save("weights/yolo11n_trained.pt")