from pathlib import Path

from app.config import TRAIN_DIR
from app.config import TEST_DIR
from app.config import CLASS_NAMES


def count_images(folder: Path) -> int:
    count = 0

    for ext in ("*.jpg", "*.jpeg", "*.png"):
        count += len(list(folder.glob(ext)))

    return count


def verify_dataset():

    print("=" * 50)
    print("Dataset Verification")
    print("=" * 50)

    if not TRAIN_DIR.exists():
        raise FileNotFoundError(TRAIN_DIR)

    if not TEST_DIR.exists():
        raise FileNotFoundError(TEST_DIR)

    train_total = 0
    test_total = 0

    for cls in CLASS_NAMES:

        train_folder = TRAIN_DIR / cls
        test_folder = TEST_DIR / cls

        train_count = count_images(train_folder)
        test_count = count_images(test_folder)

        train_total += train_count
        test_total += test_count

        print(f"{cls:<15} Train: {train_count:<5} Test: {test_count}")

    print("-" * 50)

    print(f"Training Images : {train_total}")

    print(f"Testing Images  : {test_total}")

    print("=" * 50)


if __name__ == "__main__":
    verify_dataset()