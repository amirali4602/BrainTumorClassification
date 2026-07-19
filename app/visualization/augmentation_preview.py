import tensorflow as tf
import matplotlib.pyplot as plt

from app.config import RESULTS_DIR


def save_augmentation_preview(dataset) -> None:
    """
    Save a preview of augmented images from the training dataset.
    """

    images, _ = next(iter(dataset))

    fig, axes = plt.subplots(2, 4, figsize=(12, 6))
    axes = axes.flatten()

    for i in range(8):
        image = tf.clip_by_value(images[i], 0.0, 1.0)

        axes[i].imshow(image.numpy())
        axes[i].set_title(f"Sample {i + 1}")
        axes[i].axis("off")

    plt.tight_layout()

    output_dir = RESULTS_DIR / "dataset"
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        output_dir / "augmentation_preview.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close(fig)