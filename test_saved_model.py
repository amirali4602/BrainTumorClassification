import tensorflow as tf
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image

model = load_model("saved_models/resnet50.keras")

img = image.load_img(
    "Dataset/Testing/glioma/Te-gl_0010.jpg",
    target_size=(224, 224),
)

img = image.img_to_array(img)
img = preprocess_input(img)
img = np.expand_dims(img, 0)

prediction = model.predict(img, verbose=0)

print(prediction)
print(np.argmax(prediction))