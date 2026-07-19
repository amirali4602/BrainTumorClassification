from pathlib import Path

# ===============================
# Paths
# ===============================

ROOT_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = ROOT_DIR / "dataset"

TRAIN_DIR = DATASET_DIR / "Training"

TEST_DIR = DATASET_DIR / "Testing"

MODEL_DIR = ROOT_DIR / "saved_models"

RESULTS_DIR = ROOT_DIR / "results"

REPORT_DIR = ROOT_DIR / "reports"

# ===============================
# Dataset
# ===============================

CLASS_NAMES = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

NUM_CLASSES = len(CLASS_NAMES)

# ===============================
# Image
# ===============================

IMAGE_SIZE = (224, 224)

CHANNELS = 3

# ===============================
# Training
# ===============================

BATCH_SIZE = 32

EPOCHS = 20

LEARNING_RATE = 1e-4

RANDOM_SEED = 42