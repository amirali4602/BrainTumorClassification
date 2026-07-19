from app.models.custom_cnn import CustomCNNModel
from app.models.resnet50 import ResNet50Model
from app.models.efficientnetb0 import EfficientNetB0Model


MODEL_REGISTRY = {

    "custom_cnn": CustomCNNModel,

    "resnet50": ResNet50Model,

    "efficientnetb0": EfficientNetB0Model,

}


def get_model(model_name):

    if model_name not in MODEL_REGISTRY:
        raise ValueError(
            f"Unknown model: {model_name}. "
            f"Available models: {list(MODEL_REGISTRY.keys())}"
        )

    return MODEL_REGISTRY[model_name]()