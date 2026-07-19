from app.datasets.dataset_checker import verify_dataset
from app.utils.directories import create_directories
from app.utils.logger import get_logger

logger = get_logger(__name__)


def main():

    logger.info("Brain Tumor MRI Classification")

    create_directories()

    verify_dataset()

    logger.info("Sprint 0 completed successfully.")


if __name__ == "__main__":
    main()