import tensorflow as tf

from app.config import SHUFFLE_BUFFER
from app.preprocessing.augmentations import build_augmentation

AUTOTUNE = tf.data.AUTOTUNE

augmentation = build_augmentation()


def normalize(images, labels):
    images = tf.cast(images, tf.float32) / 255.0
    return images, labels


def augment(images, labels):
    images = augmentation(images, training=True)
    return images, labels


def prepare_train(dataset):

    dataset = dataset.cache()

    dataset = dataset.shuffle(
        SHUFFLE_BUFFER,
        reshuffle_each_iteration=True,
    )

    dataset = dataset.map(
        normalize,
        num_parallel_calls=AUTOTUNE,
    )

    dataset = dataset.map(
        augment,
        num_parallel_calls=AUTOTUNE,
    )

    dataset = dataset.prefetch(AUTOTUNE)

    return dataset


def prepare_validation(dataset):

    dataset = dataset.cache()

    dataset = dataset.map(
        normalize,
        num_parallel_calls=AUTOTUNE,
    )

    dataset = dataset.prefetch(AUTOTUNE)

    return dataset


def prepare_test(dataset):

    dataset = dataset.map(
        normalize,
        num_parallel_calls=AUTOTUNE,
    )

    dataset = dataset.prefetch(AUTOTUNE)

    return dataset