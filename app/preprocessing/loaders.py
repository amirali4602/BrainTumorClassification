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

        return (
            train_dataset,
            validation_dataset,
            test_dataset,
        )