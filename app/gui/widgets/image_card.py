from PySide6.QtCore import Qt

from PySide6.QtGui import QPixmap

from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ImageCard(QWidget):

    def __init__(self, title):

        super().__init__()

        layout = QVBoxLayout(self)

        self.title = QLabel(title)

        self.title.setAlignment(Qt.AlignCenter)

        self.image = QLabel()

        self.image.setAlignment(Qt.AlignCenter)

        self.image.setMinimumHeight(250)

        layout.addWidget(self.title)

        layout.addWidget(self.image)

    def load(self, path):

        pixmap = QPixmap(str(path))

        if pixmap.isNull():
            self.image.setText("Image not found")
            return

        self.image.setPixmap(
            pixmap.scaled(
                450,
                300,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )