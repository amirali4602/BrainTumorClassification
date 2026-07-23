import json

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay

from app.config import MODELS_NAME, RESULTS_DIR


class ModelComparison:

    MODELS = MODELS_NAME

    def __init__(self):
        self.rows = []


    def load_metrics(self):

        self.rows = []

        for model in self.MODELS:

            metrics_file = (
                RESULTS_DIR /
                model /
                "metrics.json"
            )

            if not metrics_file.exists():
                continue


            with open(
                metrics_file,
                "r",
                encoding="utf-8"
            ) as file:

                metrics = json.load(file)


            self.rows.append(
                {
                    "Model": model,
                    "Accuracy": metrics["accuracy"],
                    "Precision": metrics["precision"],
                    "Recall": metrics["recall"],
                    "F1": metrics["f1"],
                }
            )


    def save_csv(self):

        df = pd.DataFrame(self.rows)

        output = (
            RESULTS_DIR /
            "model_comparison.csv"
        )

        df.to_csv(
            output,
            index=False,
        )


    def save_chart(self):

        df = pd.DataFrame(self.rows)

        metrics = [
            "Accuracy",
            "Precision",
            "Recall",
            "F1",
        ]

        for metric in metrics:

            plt.figure(figsize=(8,5))

            plt.bar(
                df["Model"],
                df[metric],
            )

            plt.title(
                f"{metric} Comparison"
            )

            plt.ylabel(metric)

            plt.ylim(
                0,
                1
            )

            plt.xticks(
                rotation=20
            )

            plt.tight_layout()


            plt.savefig(
                RESULTS_DIR /
                f"{metric.lower()}_comparison.png"
            )

            plt.close()


    def run(self):

        self.load_metrics()

        self.save_csv()

        self.save_chart()