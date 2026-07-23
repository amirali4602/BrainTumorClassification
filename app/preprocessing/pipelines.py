import tensorflow as tf

from tensorflow.keras.applications.resnet50 import (
    preprocess_input as resnet_preprocess,
)

from tensorflow.keras.applications.efficientnet import (
    preprocess_input as efficientnet_preprocess,
)

from tensorflow.keras.applications.densenet import (
    preprocess_input as densenet_preprocess,
)

from tensorflow.keras.applications.efficientnet_v2 import (
    preprocess_input as efficientnetv2_preprocess,
)

from tensorflow.keras.applications.mobilenet_v3 import (
    preprocess_input as mobilenetv3_preprocess,
)

from tensorflow.keras.applications.xception import (
    preprocess_input as xception_preprocess,
)

from tensorflow.keras.applications.convnext import (
    preprocess_input as convnext_preprocess,
)

from tensorflow.keras.applications.inception_v3 import (
    preprocess_input as inception_preprocess,
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

    elif model_name == "DenseNet121":

        images = densenet_preprocess(images)

    elif model_name == "EfficientNetV2B0":

        images = efficientnetv2_preprocess(images)

    elif model_name == "MobileNetV3 Large":

        images = mobilenetv3_preprocess(images)

    elif model_name == "Xception":

        images = xception_preprocess(images)

    elif model_name == "ConvNeXt Tiny":

            images = convnext_preprocess(images)

    elif model_name == "InceptionV3":

        images = inception_preprocess(images)
        
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