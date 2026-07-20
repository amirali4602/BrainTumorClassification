from PySide6.QtWidgets import (
    QGridLayout,
    QScrollArea,
    QWidget,
)

from app.config import RESULTS_DIR
from app.gui.widgets.image_card import ImageCard


class ComparisonGallery(QScrollArea):

    def __init__(self):
        super().__init__()

        container = QWidget()

        self.setWidget(container)
        self.setWidgetResizable(True)

        self.layout = QGridLayout(container)

        self.layout.setSpacing(15)

        self.layout.setContentsMargins(
            10,
            10,
            10,
            10,
        )

        self.cards = {}

        self.files = [
            "accuracy_comparison.png",
            "precision_comparison.png",
            "recall_comparison.png",
            "f1_comparison.png",
            "confusion_matrix_comparison.png",
        ]

        positions = {
            "accuracy_comparison.png": (0, 0),
            "precision_comparison.png": (0, 1),
            "recall_comparison.png": (1, 0),
            "f1_comparison.png": (1, 1),
            "confusion_matrix_comparison.png": (2, 0),
        }

        for filename in self.files:

            title = (
                filename
                .replace("_comparison.png", "")
                .replace("_", " ")
                .title()
            )

            card = ImageCard(title)

            self.cards[filename] = card

            row, col = positions[filename]

            if filename == "confusion_matrix_comparison.png":

                self.layout.addWidget(
                    card,
                    row,
                    col,
                    1,
                    2,
                )

            else:

                self.layout.addWidget(
                    card,
                    row,
                    col,
                )

        self.refresh()

    def refresh(self):

        for filename, card in self.cards.items():

            card.load(
                RESULTS_DIR / filename
            )