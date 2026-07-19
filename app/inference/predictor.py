import numpy as np

from app.inference.loader import ModelLoader
from app.inference.preprocessing import preprocess_image
from app.inference.result import PredictionResult


CLASS_NAMES = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary",
]


class Predictor:

    def __init__(self):

        self.loader = ModelLoader()

    def predict(
        self,
        image_path,
        model_name,
    ):

        model = self.loader.load(model_name)

        image = preprocess_image(image_path)

        prediction = model.predict(
            image,
            verbose=0,
        )[0]
        print(prediction)
        index = np.argmax(prediction)

        probabilities = {
            CLASS_NAMES[i]: float(prediction[i])
            for i in range(len(CLASS_NAMES))
        }

        return PredictionResult(
            predicted_class=CLASS_NAMES[index],
            confidence=float(prediction[index]),
            probabilities=probabilities,
        )