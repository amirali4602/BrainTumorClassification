import json

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QGridLayout,
    QTabWidget,
)
from app.gui.widgets.comparison_gallery import ComparisonGallery
from app.config import RESULTS_DIR
from app.gui.widgets.image_card import ImageCard
from app.gui.widgets.metrics_card import MetricsCard
from app.gui.widgets.comparison_table import ComparisonTable

class AnalyticsPage(QWidget):

    def __init__(self):
        super().__init__()

        self._build_ui()

    def _build_ui(self):

        main_layout = QVBoxLayout(self)

        # -----------------------------
        # Top controls
        # -----------------------------

        top = QHBoxLayout()

        top.addWidget(QLabel("Model"))

        self.model_box = QComboBox()

        self.model_box.addItem("Custom CNN", "custom_cnn")
        self.model_box.addItem("ResNet50", "resnet50")
        self.model_box.addItem("EfficientNetB0", "efficientnetb0")

        self.refresh_button = QPushButton("Refresh")

        top.addWidget(self.model_box)

        top.addStretch()

        top.addWidget(self.refresh_button)

        main_layout.addLayout(top)

        # -----------------------------
        # Analytics Tabs
        # -----------------------------

        self.tabs = QTabWidget()

        main_layout.addWidget(self.tabs)

        self.training_tab = QWidget()

        self.evaluation_tab = QWidget()

        self.comparison_tab = QWidget()

        self.tabs.addTab(
            self.training_tab,
            "Training",
        )

        self.tabs.addTab(
            self.evaluation_tab,
            "Evaluation",
        )

        self.tabs.addTab(
            self.comparison_tab,
            "Comparison",
        )

        # ===================================================
        # Training
        # ===================================================

        training_layout = QGridLayout(self.training_tab)

        self.accuracy_card = ImageCard("Accuracy")

        self.loss_card = ImageCard("Loss")

        training_layout.addWidget(
            self.accuracy_card,
            0,
            0,
        )

        training_layout.addWidget(
            self.loss_card,
            0,
            1,
        )

        # ===================================================
        # Evaluation
        # ===================================================

        evaluation_layout = QVBoxLayout(self.evaluation_tab)

        self.confusion_card = ImageCard(
            "Confusion Matrix"
        )

        self.metrics_card = MetricsCard()

        evaluation_layout.addWidget(
            self.confusion_card
        )

        evaluation_layout.addWidget(
            self.metrics_card
        )

        # ===================================================
        # Comparison
        # ===================================================

        comparison_layout = QVBoxLayout(
            self.comparison_tab
        )

        self.comparison_gallery = ComparisonGallery()

        self.comparison_table = ComparisonTable()

        comparison_layout.addWidget(
            self.comparison_gallery,
            3,
        )

        comparison_layout.addWidget(
            self.comparison_table,
            2,
        )

        # -----------------------------

        self.refresh_button.clicked.connect(
            self.load_results
        )

        self.model_box.currentIndexChanged.connect(
            self.load_results
        )

        self.load_results()

    def load_results(self):

        folder = (
            RESULTS_DIR /
            self.model_box.currentData()
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

        self.comparison_gallery.refresh()

        self.comparison_table.refresh()

        metrics_file = folder / "metrics.json"

        if metrics_file.exists():

            with open(
                metrics_file,
                encoding="utf-8",
            ) as f:

                metrics = json.load(f)

            self.metrics_card.update_metrics(
                metrics
            )

        else:

            self.metrics_card.clear()
