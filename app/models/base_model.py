from abc import ABC, abstractmethod

import tensorflow as tf


class BaseModel(ABC):
    """
    Base interface for all classification models.
    """

    def __init__(self):

        self.model = None

    @abstractmethod
    def build(self, input_shape, num_classes):
        pass

    def compile(self):

        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(),
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )

    def summary(self):

        self.model.summary()