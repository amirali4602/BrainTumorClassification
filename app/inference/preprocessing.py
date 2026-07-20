import numpy as np

from tensorflow.keras.preprocessing import image

from app.config import (
    IMAGE_HEIGHT,
    IMAGE_WIDTH,
)


def preprocess_image(image_path: str):

    img = image.load_img(
        image_path,
        target_size=(
            IMAGE_HEIGHT,
            IMAGE_WIDTH,
        ),
    )

    img = image.img_to_array(img)

    img = img / 255.0

    img = np.expand_dims(
        img,
        axis=0,
    )

    return img