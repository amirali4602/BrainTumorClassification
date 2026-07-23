import tensorflow as tf

from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Dense,
    Dropout,
    GlobalAveragePooling2D,
)

from tensorflow.keras.applications.convnext import ConvNeXtTiny

from app.models.base_model import BaseModel


class ConvNeXtTinyModel(BaseModel):

    def build(
        self,
        input_shape,
        num_classes,
    ):

        backbone = ConvNeXtTiny(
            include_top=False,
            weights="imagenet",
            input_shape=input_shape,
        )

        # Fine-tuning
        backbone.trainable = True

        # Freeze early layers
        for layer in backbone.layers[:-30]:
            layer.trainable = False

        x = backbone.output

        x = GlobalAveragePooling2D()(x)

        x = Dense(
            256,
            activation="gelu",
        )(x)

        x = Dropout(
            0.4,
        )(x)

        outputs = Dense(
            num_classes,
            activation="softmax",
        )(x)

        self.model = Model(
            inputs=backbone.input,
            outputs=outputs,
            name="ConvNeXtTiny",
        )