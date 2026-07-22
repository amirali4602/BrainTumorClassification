import tensorflow as tf

class GaussianNoise(tf.keras.layers.Layer):
    def call(self, x, training=False):
        if training:
            noise = tf.random.normal(
                shape=tf.shape(x),
                mean=0.0,
                stddev=0.02,
            )
            return x + noise
        return x

def build_augmentation():

    return tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.05),
        tf.keras.layers.RandomZoom(0.10),
        tf.keras.layers.RandomTranslation(0.05, 0.05),
        tf.keras.layers.RandomContrast(0.10),
        GaussianNoise(),
    ])