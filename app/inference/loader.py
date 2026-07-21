from tensorflow.keras.models import load_model

from app.config import MODELS_DIR


MODEL_FILES = {
    "Custom CNN": "custom_cnn.keras",
    "ResNet50": "resnet50.keras",
    "EfficientNetB0": "efficientnetb0.keras",
}


class ModelLoader:

    def __init__(self):
        self._cache = {}

    def load(self, model_name):

        if model_name in self._cache:
            return self._cache[model_name]

        path = MODELS_DIR / MODEL_FILES[model_name]

        if not path.exists():
            print(f"Model not found: {path}")
            return None

        model = load_model(path)

        self._cache[model_name] = model

        print(f"Loading model: {path}")

        return model