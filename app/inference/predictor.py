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

    def __init__(
        self,
        model_name="Custom CNN",
    ):

        self.loader = ModelLoader()

        self.model = None

        self.current_model = None

        self.reload(model_name)

    def predict(self, image_path):

        image = preprocess_image(
            image_path,
            self.current_model,
        )

        prediction = self.model.predict(
            image,
            verbose=0,
        )[0]

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

    def reload(self, model_name):

        self.current_model = model_name

        self.model = self.loader.load(model_name)