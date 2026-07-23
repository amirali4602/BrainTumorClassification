from app.models.custom_cnn import CustomCNNModel
from app.models.densenet121 import DenseNet121Model
from app.models.efficientnetv2b0 import EfficientNetV2B0Model
from app.models.inception_v3 import InceptionV3Model
from app.models.mobilenetv3 import MobileNetV3LargeModel
from app.models.resnet50 import ResNet50Model
from app.models.efficientnetb0 import EfficientNetB0Model
from app.models.xception import XceptionModel
from app.models.convnext_tiny import ConvNeXtTinyModel

MODEL_REGISTRY = {
    "custom_cnn": CustomCNNModel,
    "resnet50": ResNet50Model,
    "efficientnetb0": EfficientNetB0Model,
    "densenet121": DenseNet121Model,
    "efficientnetv2b0": EfficientNetV2B0Model,
    "xception": XceptionModel,
    "mobilenetv3": MobileNetV3LargeModel,
    "convnext_tiny": ConvNeXtTinyModel,
    "inceptionv3": InceptionV3Model
}


def get_model(model_name):

    if model_name not in MODEL_REGISTRY:
        raise ValueError(
            f"Unknown model: {model_name}. "
            f"Available models: {list(MODEL_REGISTRY.keys())}"
        )

    return MODEL_REGISTRY[model_name]()