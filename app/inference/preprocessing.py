import numpy as np

from tensorflow.keras.preprocessing import image

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

    elif model_name == "DenseNet121":

        img = densenet_preprocess(img)

    elif model_name == "EfficientNetV2B0":

        img = efficientnetv2_preprocess(img)

    elif model_name == "MobileNetV3 Large":

        img = mobilenetv3_preprocess(img)

    elif model_name == "Xception":

        img = xception_preprocess(img)

    elif model_name == "ConvNeXt Tiny":

        images = convnext_preprocess(img)
        
    elif model_name == "InceptionV3":

        img = inception_preprocess(img)

    else:

        img = img / 255.0

    img = np.expand_dims(
        img,
        axis=0,
    )

    return img