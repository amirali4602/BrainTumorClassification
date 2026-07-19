from pathlib import Path
import random

import matplotlib.pyplot as plt
from PIL import Image

from app.config import RESULTS_DIR


OUTPUT = RESULTS_DIR / "dataset"


def plot_class_distribution(counter):

    OUTPUT.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))

    plt.bar(counter.keys(), counter.values())

    plt.title("Training Dataset Distribution")

    plt.tight_layout()

    plt.savefig(OUTPUT / "class_distribution.png")

    plt.close()


def plot_image_sizes(sizes):

    OUTPUT.mkdir(parents=True, exist_ok=True)

    widths = [w for w, _ in sizes]
    heights = [h for _, h in sizes]

    plt.figure(figsize=(8, 5))

    plt.scatter(widths, heights)

    plt.xlabel("Width")

    plt.ylabel("Height")

    plt.title("Image Size Distribution")

    plt.tight_layout()

    plt.savefig(OUTPUT / "image_size_distribution.png")

    plt.close()


def plot_samples(images, labels, n=8):

    OUTPUT.mkdir(parents=True, exist_ok=True)

    samples = random.sample(list(zip(images, labels)), n)

    fig, axes = plt.subplots(2, 4, figsize=(12, 6))

    axes = axes.flatten()

    for ax, (img_path, label) in zip(axes, samples):

        image = Image.open(img_path)

        ax.imshow(image)

        ax.set_title(label)

        ax.axis("off")

    plt.tight_layout()

    plt.savefig(OUTPUT / "sample_images.png")

    plt.close()