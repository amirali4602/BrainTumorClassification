from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class HistoryManager:

    def __init__(self, history, output_dir: Path):

        self.history = history
        self.output_dir = output_dir

        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_csv(self):

        pd.DataFrame(
            self.history.history
        ).to_csv(
            self.output_dir / "history.csv",
            index=False,
        )

    def plot_accuracy(self):

        plt.figure(figsize=(8, 5))

        plt.plot(self.history.history["accuracy"], label="Training")
        plt.plot(self.history.history["val_accuracy"], label="Validation")

        plt.title("Accuracy")
        plt.xlabel("Epoch")
        plt.ylabel("Accuracy")
        plt.grid(True)
        plt.legend()

        plt.savefig(self.output_dir / "accuracy.png", dpi=300)
        plt.close()

    def plot_loss(self):

        plt.figure(figsize=(8, 5))

        plt.plot(self.history.history["loss"], label="Training")
        plt.plot(self.history.history["val_loss"], label="Validation")

        plt.title("Loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.grid(True)
        plt.legend()

        plt.savefig(self.output_dir / "loss.png", dpi=300)
        plt.close()

    def save_all(self):

        self.save_csv()
        self.plot_accuracy()
        self.plot_loss()