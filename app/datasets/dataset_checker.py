from pathlib import Path

from app.config import (
    TRAIN_DIR,
    TEST_DIR,
    CLASS_NAMES,
)

from app.utils.logger import get_logger

logger = get_logger(__name__)


def count_images(folder: Path) -> int:

    count = 0

    for ext in ("*.jpg", "*.jpeg", "*.png"):
        count += len(list(folder.glob(ext)))

    return count


def verify_dataset():

    logger.info("=" * 60)
    logger.info("Dataset Verification")
    logger.info("=" * 60)

    train_total = 0
    test_total = 0

    for cls in CLASS_NAMES:

        train_folder = TRAIN_DIR / cls
        test_folder = TEST_DIR / cls

        train_count = count_images(train_folder)
        test_count = count_images(test_folder)

        train_total += train_count
        test_total += test_count

        logger.info(
            f"{cls:<15} Train: {train_count:<5} Test: {test_count}"
        )

    logger.info("-" * 60)

    logger.info(f"Training Images : {train_total}")

    logger.info(f"Testing Images  : {test_total}")

    logger.info("=" * 60)