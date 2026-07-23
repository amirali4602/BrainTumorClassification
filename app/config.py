from pathlib import Path

import tensorflow as tf

ROOT_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = ROOT_DIR / "dataset"


TRAIN_DIR = DATASET_DIR / "Training"

TEST_DIR = DATASET_DIR / "Testing"

SAVED_MODELS_DIR = ROOT_DIR / "saved_models"

RESULTS_DIR = ROOT_DIR / "results"

REPORTS_DIR = ROOT_DIR / "reports"

LOGS_DIR = ROOT_DIR / "logs"

LOGO_DIR = "app/gui/resources/images/Logo.jpg"

MODEL_FILES = {
    "Custom CNN": "custom_cnn.keras",
    "ResNet50": "resnet50.keras",
    "EfficientNetB0": "efficientnetb0.keras",
    "DenseNet121": "densenet121.keras",
    "EfficientNetV2B0": "efficientnetv2b0.keras",
    "MobileNetV3 Large": "mobilenetv3.keras",
    "Xception": "xception.keras",
    "ConvNeXt Tiny" : "convnext_tiny.keras",
    "InceptionV3" : "inceptionv3.keras"
}

MODELS_NAME = [
    "custom_cnn",
    "resnet50",
    "efficientnetb0",
    "densenet121",
    "efficientnetv2b0",
    "mobilenetv3",
    "xception",
    "convnext_tiny",
    "inceptionv3"
]

MODELS = [
    "Custom CNN",
    "ResNet50",
    "EfficientNetB0",
    "DenseNet121",
    "EfficientNetV2B0",
    "MobileNetV3 Large",
    "Xception",
    "ConvNeXt Tiny",
    "InceptionV3"
]

CLASS_NAMES = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary",
]

VALID_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
}

MODEL_NAME = "convnext_tiny"

NUM_CLASSES = len(CLASS_NAMES)

# ===============================
# Image
# ===============================

IMAGE_HEIGHT = 299
IMAGE_WIDTH = 299
IMAGE_SIZE = (IMAGE_HEIGHT, IMAGE_WIDTH)

CHANNELS = 3

# ===============================
# Dataset
# ===============================

BATCH_SIZE = 32

VALIDATION_SPLIT = 0.2

SHUFFLE_BUFFER = 1000

AUTOTUNE = tf.data.AUTOTUNE

# ===============================
# Training
# ===============================

EPOCHS = 50

LEARNING_RATE = 1e-5

WEIGHT_DECAY = 1e-4

RANDOM_SEED = 42

# ===============================
# Models
# ===============================
MODELS_DIR = ROOT_DIR / "saved_models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)