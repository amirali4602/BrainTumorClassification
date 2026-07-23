from app.models.convnext_tiny import ConvNeXtTinyModel
from app.models.custom_cnn import CustomCNNModel
from app.models.densenet121 import DenseNet121Model
from app.models.efficientnetv2b0 import EfficientNetV2B0Model
from app.models.inception_v3 import InceptionV3Model
from app.models.mobilenetv3 import MobileNetV3LargeModel
from app.models.resnet50 import ResNet50Model
from app.models.efficientnetb0 import EfficientNetB0Model

from app.models.xception import XceptionModel
from app.training.runner import TrainingRunner


class ModelRetrainer:

    def __init__(self):

        self.models = {
            "Custom CNN": (
                CustomCNNModel,
                "custom_cnn",
            ),
            "ResNet50": (
                ResNet50Model,
                "resnet50",
            ),
            "EfficientNetB0": (
                EfficientNetB0Model,
                "efficientnetb0",
            ),
            "DenseNet121": (
                DenseNet121Model,
                "densenet121",
            ),
            "EfficientNetV2B0": (
                EfficientNetV2B0Model,
                "efficientnetv2b0",
            ),
            "Xception": (
                XceptionModel,
                "xception",
            ),
            "MobileNetV3 Large": (
                MobileNetV3LargeModel,
                "mobilenetv3",
            ),
            "ConvNeXt Tiny": (
                ConvNeXtTinyModel,
                "convnext_tiny",
            ),
            "InceptionV3": (
                InceptionV3Model,
                "inceptionv3",
            ),
        }

    def train(
        self,
        model_name,
        epochs,
    ):

        model_class, folder = self.models[model_name]

        runner = TrainingRunner(
            model=model_class(),
            model_name=folder,
            epochs=epochs,
        )

        runner.run()