import tensorflow as tf

from tensorflow.keras.applications.resnet50 import (
    preprocess_input as resnet_preprocess,
)

from tensorflow.keras.applications.efficientnet import (
    preprocess_input as efficientnet_preprocess,
)

from app.config import SHUFFLE_BUFFER
from app.preprocessing.augmentations import build_augmentation

AUTOTUNE = tf.data.AUTOTUNE

augmentation = build_augmentation()


def normalize(images, labels, model_name):

    images = tf.cast(images, tf.float32)

    if model_name == "Custom CNN":

        images = images / 255.0

    elif model_name == "ResNet50":

        images = resnet_preprocess(images)

    elif model_name == "EfficientNetB0":

        images = efficientnet_preprocess(images)

    else:

        images = images / 255.0

    return images, labels


def augment(images, labels):

    images = augmentation(images, training=True)

    return images, labels


def prepare_train(dataset, model_name):

    dataset = dataset.cache()

    dataset = dataset.shuffle(
        SHUFFLE_BUFFER,
        reshuffle_each_iteration=True,
    )

    dataset = dataset.map(
        lambda x, y: normalize(
            x,
            y,
            model_name,
        ),
        num_parallel_calls=AUTOTUNE,
    )

    dataset = dataset.map(
        augment,
        num_parallel_calls=AUTOTUNE,
    )

    dataset = dataset.prefetch(AUTOTUNE)

    return dataset


def prepare_validation(dataset, model_name):

    dataset = dataset.cache()

    dataset = dataset.map(
        lambda x, y: normalize(
            x,
            y,
            model_name,
        ),
        num_parallel_calls=AUTOTUNE,
    )

    dataset = dataset.prefetch(AUTOTUNE)

    return dataset


def prepare_test(dataset, model_name):

    dataset = dataset.map(
        lambda x, y: normalize(
            x,
            y,
            model_name,
        ),
        num_parallel_calls=AUTOTUNE,
    )

    dataset = dataset.prefetch(AUTOTUNE)

    return dataset