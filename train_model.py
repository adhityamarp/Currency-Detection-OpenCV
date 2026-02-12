import os
import splitfolders # pip install split-folders
from ultralytics import YOLO

# 1. Split your folders into Train/Val automatically
input_folder = "Dataset" # The folder containing your 10, 20, 100 folders
splitfolders.ratio(input_folder, output="processed_data", seed=1337, ratio=(.8, .2))

# 2. Train the Classification Model
# We use 'yolov8n-cls.pt' (the -cls stands for classification)
model = YOLO('yolov8n-cls.pt')

# Train for 20 epochs
model.train(data='processed_data', epochs=20, imgsz=224)