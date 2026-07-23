from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
)

from app.gui.widgets.image_view import ImageView
from app.gui.widgets.prediction_panel import PredictionPanel


class PredictionPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            15,
            15,
            15,
            15,
        )

        self.image_view = ImageView()

        self.prediction_panel = PredictionPanel()

        layout.addWidget(
            self.image_view,
            3,
        )

        layout.addWidget(
            self.prediction_panel,
            1,
        )