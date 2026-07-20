from app.models.custom_cnn import CustomCNNModel
from app.models.resnet50 import ResNet50Model
from app.models.efficientnetb0 import EfficientNetB0Model

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