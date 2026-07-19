from app.preprocessing.loaders import DatasetLoader
from app.preprocessing.pipelines import (
    prepare_train,
    prepare_test,
)
from app.preprocessing.pipeline_report import save_pipeline_report
from app.visualization.augmentation_preview import save_augmentation_preview
from app.utils.logger import get_logger

logger = get_logger(__name__)


def main():

    loader = DatasetLoader()

    train_ds, val_ds, test_ds = loader.load()

    train_ds = prepare_train(train_ds)

    val_ds = prepare_test(val_ds)

    test_ds = prepare_test(test_ds)
    save_augmentation_preview(train_ds)

    save_pipeline_report()

    logger.info("Training batches : %d", len(train_ds))

    logger.info("Validation batches : %d", len(val_ds))

    logger.info("Testing batches : %d", len(test_ds))

    images, labels = next(iter(train_ds))

    logger.info("Image batch shape : %s", images.shape)

    logger.info("Label batch shape : %s", labels.shape)


if __name__ == "__main__":
    main()