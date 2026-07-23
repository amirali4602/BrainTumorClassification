from tensorflow.keras.utils import image_dataset_from_directory

from app.config import (
    TRAIN_DIR,
    TEST_DIR,
    IMAGE_SIZE,
    BATCH_SIZE,
    VALIDATION_SPLIT,
    RANDOM_SEED,
)


class DatasetLoader:

    def __init__(self):
        self.class_names = None

    def load(self):

        train_dataset = image_dataset_from_directory(
            TRAIN_DIR,
            validation_split=VALIDATION_SPLIT,
            subset="training",
            seed=RANDOM_SEED,
            image_size=IMAGE_SIZE,
            batch_size=BATCH_SIZE,
        )

        validation_dataset = image_dataset_from_directory(
            TRAIN_DIR,
            validation_split=VALIDATION_SPLIT,
            subset="validation",
            seed=RANDOM_SEED,
            image_size=IMAGE_SIZE,
            batch_size=BATCH_SIZE,
        )

        test_dataset = image_dataset_from_directory(
            TEST_DIR,
            shuffle=False,
            image_size=IMAGE_SIZE,
            batch_size=BATCH_SIZE,
        )

        # Save class names for later use
        self.class_names = train_dataset.class_names
        print(train_dataset.class_names)
        return (
            train_dataset,
            validation_dataset,
            test_dataset,
        )