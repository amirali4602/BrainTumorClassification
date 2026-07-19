import tensorflow as tf

from app.models.base_model import BaseModel


class CustomCNNModel(BaseModel):

    def build(self, input_shape, num_classes):

        self.model = tf.keras.Sequential(
            [
                tf.keras.layers.Input(shape=input_shape),

                tf.keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.MaxPooling2D(),

                tf.keras.layers.Conv2D(64, 3, padding="same", activation="relu"),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.MaxPooling2D(),

                tf.keras.layers.Conv2D(128, 3, padding="same", activation="relu"),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.MaxPooling2D(),

                tf.keras.layers.GlobalAveragePooling2D(),

                tf.keras.layers.Dense(128, activation="relu"),
                tf.keras.layers.Dropout(0.5),

                tf.keras.layers.Dense(
                    num_classes,
                    activation="softmax",
                ),
            ],
            name="CustomCNN",
        )

        return self.model