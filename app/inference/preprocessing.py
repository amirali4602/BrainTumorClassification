import numpy as np

from tensorflow.keras.preprocessing import image

from tensorflow.keras.applications.resnet50 import (
    preprocess_input as resnet_preprocess,
)

from tensorflow.keras.applications.efficientnet import (
    preprocess_input as efficientnet_preprocess,
)

from app.config import (
    IMAGE_HEIGHT,
    IMAGE_WIDTH,
)


def preprocess_image(
    image_path: str,
    model_name: str,
):

    img = image.load_img(
        image_path,
        target_size=(
            IMAGE_HEIGHT,
            IMAGE_WIDTH,
        ),
    )

    img = image.img_to_array(img)

    if model_name == "Custom CNN":

        img = img / 255.0

    elif model_name == "ResNet50":

        img = resnet_preprocess(img)

    elif model_name == "EfficientNetB0":

        img = efficientnet_preprocess(img)

    else:

        img = img / 255.0

    img = np.expand_dims(
        img,
        axis=0,
    )

    return img