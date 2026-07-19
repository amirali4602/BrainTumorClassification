from pathlib import Path

from app.config import CLASS_NAMES


class DatasetLoader:
    """
    Loads image paths and labels from a dataset directory.
    """

    IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}

    def __init__(self, dataset_dir: Path):
        self.dataset_dir = Path(dataset_dir)

    def load(self):
        images = []
        labels = []

        for label in CLASS_NAMES:

            class_dir = self.dataset_dir / label

            if not class_dir.exists():
                continue

            for image in sorted(class_dir.iterdir()):

                if image.suffix.lower() not in self.IMAGE_EXTENSIONS:
                    continue

                images.append(image)
                labels.append(label)

        return images, labels