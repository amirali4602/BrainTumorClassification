from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QDialog,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QGraphicsView,
    QVBoxLayout,
)


class ImageViewer(QDialog):

    def __init__(self, image_path, parent=None):

        super().__init__(parent)

        self.setWindowTitle(Path(image_path).name)

        self.resize(1200, 900)

        self.zoom = 1.0

        layout = QVBoxLayout(self)

        self.scene = QGraphicsScene()

        self.view = QGraphicsView(self.scene)

        self.view.setRenderHints(
            self.view.renderHints()
        )

        layout.addWidget(self.view)

        pixmap = QPixmap(image_path)

        self.item = QGraphicsPixmapItem(pixmap)

        self.scene.addItem(self.item)

        self.view.fitInView(
            self.item,
            Qt.KeepAspectRatio,
        )

    def wheelEvent(self, event):

        if event.angleDelta().y() > 0:

            factor = 1.15

        else:

            factor = 1 / 1.15

        self.zoom *= factor

        self.view.scale(
            factor,
            factor,
        )