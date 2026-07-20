from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class ImageView(QWidget):

    def __init__(self):
        super().__init__()

        self.current_pixmap = None

        layout = QVBoxLayout(self)

        self.image_label = QLabel("No Image Loaded")

        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(600, 600)

        layout.addWidget(self.image_label)

    def set_image(self, filename):

        pixmap = QPixmap(filename)

        self.current_pixmap = pixmap

        self._update_pixmap()

    def clear(self):

        self.current_pixmap = None

        self.image_label.setPixmap(QPixmap())

        self.image_label.setText("No Image Loaded")

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self._update_pixmap()

    def _update_pixmap(self):

        if self.current_pixmap is None:
            return

        scaled = self.current_pixmap.scaled(
            self.image_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )

        self.image_label.setPixmap(scaled)