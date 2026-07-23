from tensorflow.keras.models import Model

from tensorflow.keras.layers import (
    Dense,
    Dropout,
    GlobalAveragePooling2D,
)

from tensorflow.keras.applications import MobileNetV3Large

from app.models.base_model import BaseModel


class MobileNetV3LargeModel(BaseModel):

    def build(
        self,
        input_shape,
        num_classes,
    ):

        backbone = MobileNetV3Large(
            weights="imagenet",
            include_top=False,
            input_shape=input_shape,
        )

        backbone.trainable = True

        # Freeze most layers
        for layer in backbone.layers[:-30]:
            layer.trainable = False

        x = backbone.output

        x = GlobalAveragePooling2D()(x)

        x = Dense(
            256,
            activation="relu",
        )(x)

        x = Dropout(
            0.5,
        )(x)

        outputs = Dense(
            num_classes,
            activation="softmax",
        )(x)

        self.model = Model(
            inputs=backbone.input,
            outputs=outputs,
            name="MobileNetV3Large",
        )