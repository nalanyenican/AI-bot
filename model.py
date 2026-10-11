import h5py
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os

def get_class(image_path, model_path="keras_model.h5", labels_path="labels.txt"):
    # Türkçe karakter sorununu aşmak için mutlak yol alıp h5py ile yüklüyoruz
    abs_model_path = os.path.abspath(model_path)
    with h5py.File(abs_model_path, 'r') as f:
        model = load_model(f, compile=False)
        
    class_names = open(labels_path, "r", encoding="utf-8").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    
    return class_name[2:].strip(), confidence_score