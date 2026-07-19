from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = ROOT_DIR / "dataset"

TRAIN_DIR = DATASET_DIR / "Training"

TEST_DIR = DATASET_DIR / "Testing"

SAVED_MODELS_DIR = ROOT_DIR / "saved_models"

RESULTS_DIR = ROOT_DIR / "results"

REPORTS_DIR = ROOT_DIR / "reports"

LOGS_DIR = ROOT_DIR / "logs"

CLASS_NAMES = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary",
]

NUM_CLASSES = len(CLASS_NAMES)

IMAGE_SIZE = (224, 224)

CHANNELS = 3

BATCH_SIZE = 32

EPOCHS = 20

LEARNING_RATE = 1e-4

RANDOM_SEED = 42