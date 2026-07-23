import math
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import ConfusionMatrixDisplay

from app.config import MODELS_NAME, RESULTS_DIR


class ConfusionComparison:

    MODELS = MODELS_NAME

    def run(self):

        cols = 3
        rows = math.ceil(len(self.MODELS) / cols)

        fig, axes = plt.subplots(
            rows,
            cols,
            figsize=(6 * cols, 5 * rows),
        )

        axes = np.array(axes).reshape(-1)

        for ax, model_name in zip(axes, self.MODELS):

            path = (
                RESULTS_DIR /
                model_name /
                "confusion_matrix.npy"
            )

            if not path.exists():
                ax.axis("off")
                continue

            cm = np.load(path)

            display = ConfusionMatrixDisplay(
                confusion_matrix=cm,
                display_labels=[
                    "glioma",
                    "meningioma",
                    "notumor",
                    "pituitary",
                ],
            )

            display.plot(
                ax=ax,
                values_format="d",
                colorbar=False,
            )

            ax.set_title(model_name)

        # Hide unused axes
        for ax in axes[len(self.MODELS):]:
            ax.axis("off")

        plt.tight_layout()

        plt.savefig(
            RESULTS_DIR /
            "confusion_matrix_comparison.png",
            dpi=300,
        )

        plt.close()