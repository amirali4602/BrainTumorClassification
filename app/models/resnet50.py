import tensorflow as tf

from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Dense,
    Dropout,
    GlobalAveragePooling2D,
)

from tensorflow.keras.applications import ResNet50

from app.models.base_model import BaseModel


class ResNet50Model(BaseModel):

    def build(
        self,
        input_shape,
        num_classes,
    ):

        backbone = ResNet50(
            weights="imagenet",
            include_top=False,
            input_shape=input_shape,
        )

        backbone.trainable = False


        x = backbone.output

        x = GlobalAveragePooling2D()(x)

        x = Dense(
            256,
            activation="relu",
        )(x)

        x = Dropout(
            0.5
        )(x)

        output = Dense(
            num_classes,
            activation="softmax",
        )(x)


        self.model = Model(
            inputs=backbone.input,
            outputs=output,
            name="ResNet50",
        )