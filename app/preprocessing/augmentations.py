import tensorflow as tf


def build_augmentation():

    return tf.keras.Sequential([
        tf.keras.layers.RandomRotation(0.03),
        tf.keras.layers.RandomZoom(0.05),
        tf.keras.layers.RandomContrast(0.05),
    ])