from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = ROOT_DIR / "dataset"


TRAIN_DIR = DATASET_DIR / "Training"

TEST_DIR = DATASET_DIR / "Testing"

SAVED_MODELS_DIR = ROOT_DIR / "saved_models"

RESULTS_DIR = ROOT_DIR / "results"

REPORTS_DIR = ROOT_DIR / "reports"

LOGS_DIR = ROOT_DIR / "logs"

LOGO_DIR = "app/gui/resources/images/Logo.jpg"

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

MODEL_NAME = "efficientnetb0"

NUM_CLASSES = len(CLASS_NAMES)

# ===============================
# Image
# ===============================

IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224
IMAGE_SIZE = (IMAGE_HEIGHT, IMAGE_WIDTH)

CHANNELS = 3

# ===============================
# Dataset
# ===============================

BATCH_SIZE = 32

VALIDATION_SPLIT = 0.2

SHUFFLE_BUFFER = 1000

AUTOTUNE = -1

# ===============================
# Training
# ===============================

EPOCHS = 20

LEARNING_RATE = 1e-4

RANDOM_SEED = 42

# ===============================
# Models
# ===============================
MODELS_DIR = ROOT_DIR / "saved_models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)