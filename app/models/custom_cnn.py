import tensorflow as tf

from app.models.base_model import BaseModel


class CustomCNNModel(BaseModel):

    def build(self, input_shape, num_classes):

        l2 = tf.keras.regularizers.l2(1e-4)

        self.model = tf.keras.Sequential(
            [
                tf.keras.layers.Input(shape=input_shape),

                # Block 1
                tf.keras.layers.Conv2D(
                    32,
                    3,
                    padding="same",
                    use_bias=False,
                    kernel_regularizer=l2,
                ),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.ReLU(),

                tf.keras.layers.Conv2D(
                    32,
                    3,
                    padding="same",
                    use_bias=False,
                    kernel_regularizer=l2,
                ),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.ReLU(),

                tf.keras.layers.MaxPooling2D(),
                tf.keras.layers.Dropout(0.20),

                # Block 2
                tf.keras.layers.Conv2D(
                    64,
                    3,
                    padding="same",
                    use_bias=False,
                    kernel_regularizer=l2,
                ),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.ReLU(),

                tf.keras.layers.Conv2D(
                    64,
                    3,
                    padding="same",
                    use_bias=False,
                    kernel_regularizer=l2,
                ),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.ReLU(),

                tf.keras.layers.MaxPooling2D(),
                tf.keras.layers.Dropout(0.25),

                # Block 3
                tf.keras.layers.Conv2D(
                    128,
                    3,
                    padding="same",
                    use_bias=False,
                    kernel_regularizer=l2,
                ),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.ReLU(),

                tf.keras.layers.Conv2D(
                    128,
                    3,
                    padding="same",
                    use_bias=False,
                    kernel_regularizer=l2,
                ),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.ReLU(),

                tf.keras.layers.MaxPooling2D(),
                tf.keras.layers.Dropout(0.30),

                # Block 4
                tf.keras.layers.Conv2D(
                    256,
                    3,
                    padding="same",
                    use_bias=False,
                    kernel_regularizer=l2,
                ),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.ReLU(),

                tf.keras.layers.MaxPooling2D(),

                tf.keras.layers.GlobalAveragePooling2D(),

                tf.keras.layers.BatchNormalization(),

                tf.keras.layers.Dense(
                    256,
                    activation="relu",
                    kernel_regularizer=tf.keras.regularizers.l2(1e-4),
                ),

                tf.keras.layers.Dropout(0.5),

                tf.keras.layers.Dense(
                    num_classes,
                    activation="softmax",
                    kernel_regularizer=tf.keras.regularizers.l2(1e-4),
                ),
            ],
            name="CustomCNN",
        )

        return self.model