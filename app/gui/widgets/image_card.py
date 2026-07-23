from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from app.gui.dialogs.image_viewer import ImageViewer


class ImageCard(QWidget):

    def __init__(self, title):

        super().__init__()

        layout = QVBoxLayout(self)

        self.title = QLabel(title)

        self.title.setAlignment(Qt.AlignCenter)

        self.image = QLabel()

        self.image.setAlignment(Qt.AlignCenter)

        self.image.setMinimumSize(
            300,
            450,
        )

        layout.addWidget(self.title)

        layout.addWidget(
            self.image,
            1,
        )

        self.pixmap = None

        self.image_path = None

        self.image.mouseDoubleClickEvent = (
            self.open_viewer
        )

    def load(self, path):

        path = Path(path)

        self.image_path = str(path)

        if not path.exists():

            self.image.setText(
                "Image not found"
            )

            self.pixmap = None

            return

        self.pixmap = QPixmap(str(path))

        self.update_pixmap()

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_pixmap()

    def update_pixmap(self):

        if self.pixmap is None:

            return

        self.image.setPixmap(

            self.pixmap.scaled(

                self.image.size(),

                Qt.KeepAspectRatio,

                Qt.SmoothTransformation,

            )

        )

    def open_viewer(self, event):

        if self.image_path is None:

            return

        viewer = ImageViewer(
            self.image_path,
            self,
        )

        viewer.exec()