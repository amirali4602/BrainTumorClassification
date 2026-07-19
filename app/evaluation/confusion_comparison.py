import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import ConfusionMatrixDisplay

from app.config import RESULTS_DIR


class ConfusionComparison:


    MODELS = [
        "custom_cnn",
        "resnet50",
        "efficientnetb0",
    ]


    def run(self):

        fig, axes = plt.subplots(
            1,
            3,
            figsize=(18,5)
        )


        for ax, model_name in zip(
            axes,
            self.MODELS
        ):

            path = (
                RESULTS_DIR /
                model_name /
                "confusion_matrix.npy"
            )


            if not path.exists():
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
            )


            ax.set_title(
                model_name
            )


        plt.tight_layout()


        plt.savefig(
            RESULTS_DIR /
            "confusion_matrix_comparison.png"
        )


        plt.close()