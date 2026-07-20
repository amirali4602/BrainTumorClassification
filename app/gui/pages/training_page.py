from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class TrainingPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel(
            "Training page\n(Coming in Sprint 8)"
        )

        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)