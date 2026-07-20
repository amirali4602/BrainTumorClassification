import json
from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QComboBox,
)
from app.gui.widgets.metrics_card import MetricsCard
from app.config import RESULTS_DIR
from app.gui.widgets.image_card import ImageCard


class AnalyticsPage(QWidget):

    def __init__(self):
        super().__init__()

        self._build_ui()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        top = QHBoxLayout()

        top.addWidget(QLabel("Model"))

        self.model_box = QComboBox()

        self.model_box.addItems([
            "custom_cnn",
            "resnet50",
            "efficientnetb0",
        ])

        self.refresh_button = QPushButton("Refresh")

        top.addWidget(self.model_box)

        top.addStretch()

        top.addWidget(self.refresh_button)

        layout.addLayout(top)

        grid = QGridLayout()

        self.accuracy_card = ImageCard("Accuracy")

        self.loss_card = ImageCard("Loss")

        self.confusion_card = ImageCard("Confusion Matrix")

        self.metrics_card = MetricsCard()

        grid.addWidget(
            self.accuracy_card,
            0,
            0,
        )

        grid.addWidget(
            self.loss_card,
            0,
            1,
        )

        grid.addWidget(
            self.confusion_card,
            1,
            0,
            1,
            2,
        )

        layout.addLayout(grid)

        self.refresh_button.clicked.connect(
            self.load_results
        )

        self.model_box.currentIndexChanged.connect(
            self.load_results
        )
        layout.addWidget(self.metrics_card)
        self.load_results()

    def load_results(self):

        folder = (
            RESULTS_DIR /
            self.model_box.currentText()
        )

        self.accuracy_card.load(
            folder / "accuracy.png"
        )

        self.loss_card.load(
            folder / "loss.png"
        )

        self.confusion_card.load(
            folder / "confusion_matrix.png"
        )

        metrics_file = folder / "metrics.json"

        if metrics_file.exists():

            with open(metrics_file) as f:
                metrics = json.load(f)

            self.metrics_card.update_metrics(metrics)

        else:

            self.metrics_card.clear()