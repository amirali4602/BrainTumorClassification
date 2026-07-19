from app.config import TRAIN_DIR
from app.datasets.dataset_analyzer import DatasetAnalyzer
from app.datasets.dataset_checker import verify_dataset
from app.datasets.report_generator import DatasetReport
from app.utils.directories import create_directories
from app.utils.logger import get_logger
from app.visualization.plots import (
    plot_class_distribution,
    plot_image_sizes,
    plot_samples,
)

logger = get_logger(__name__)


def main():

    logger.info("Brain Tumor MRI Classification")

    create_directories()

    verify_dataset()

    analyzer = DatasetAnalyzer(TRAIN_DIR)

    distribution = analyzer.class_distribution()

    sizes = analyzer.image_sizes()

    avg = analyzer.average_size()

    minimum = analyzer.min_size()

    maximum = analyzer.max_size()

    logger.info("Dataset Summary")
    logger.info("Average Size : %.2f x %.2f", *avg)
    logger.info("Minimum Size : %s", minimum)
    logger.info("Maximum Size : %s", maximum)

    plot_class_distribution(distribution)
    plot_image_sizes(sizes)
    plot_samples(analyzer.images, analyzer.labels)

    report = DatasetReport()

    report.save_csv(distribution)

    report.save_markdown(
        distribution,
        avg,
        minimum,
        maximum,
    )

    logger.info("Sprint 1 completed successfully.")


if __name__ == "__main__":
    main()