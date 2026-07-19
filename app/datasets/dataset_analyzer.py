from collections import Counter

import numpy as np
from PIL import Image

from app.datasets.dataset_loader import DatasetLoader


class DatasetAnalyzer:

    def __init__(self, dataset_dir):

        self.loader = DatasetLoader(dataset_dir)

        self.images, self.labels = self.loader.load()

    def class_distribution(self):

        return Counter(self.labels)

    def image_sizes(self):

        sizes = []

        for image_path in self.images:

            with Image.open(image_path) as img:
                sizes.append(img.size)

        return sizes

    def average_size(self):

        sizes = self.image_sizes()

        widths = [w for w, _ in sizes]
        heights = [h for _, h in sizes]

        return np.mean(widths), np.mean(heights)

    def min_size(self):

        sizes = self.image_sizes()

        widths = [w for w, _ in sizes]
        heights = [h for _, h in sizes]

        return min(widths), min(heights)

    def max_size(self):

        sizes = self.image_sizes()

        widths = [w for w, _ in sizes]
        heights = [h for _, h in sizes]

        return max(widths), max(heights)