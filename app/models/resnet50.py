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

        backbone.trainable = True

        for layer in backbone.layers[:-30]:
            layer.trainable = False


        x = backbone.output

        x = GlobalAveragePooling2D()(x)

        x = Dense(
            256,
            activation="relu",
            kernel_regularizer=tf.keras.regularizers.l2(1e-4),
        )(x)

        x = Dropout(
            0.5
        )(x)

        output = Dense(
            num_classes,
            activation="softmax",
            kernel_regularizer=tf.keras.regularizers.l2(1e-4),
        )(x)


        self.model = Model(
            inputs=backbone.input,
            outputs=output,
            name="ResNet50",
        )