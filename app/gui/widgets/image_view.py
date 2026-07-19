from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class ImageView(QWidget):

    def __init__(self):
        super().__init__()

        self.pixmap = None

        self.image_label = QLabel("MRI Image\n\nLoad an image to begin")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.image_label.setMinimumSize(600, 600)

        self.image_label.setStyleSheet("""
            QLabel {
                border: 2px dashed #555;
                border-radius: 12px;
                font-size: 18px;
                color: #BBBBBB;
                background-color: #2B2D42;
            }
        """)

        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)

    def set_image(self, image_path: str):

        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            return

        self.pixmap = pixmap

        self._update_pixmap()

    def clear(self):

        self.pixmap = None

        self.image_label.setPixmap(QPixmap())

        self.image_label.setText("MRI Image\n\nLoad an image to begin")

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self._update_pixmap()

    def _update_pixmap(self):

        if self.pixmap is None:
            return

        scaled = self.pixmap.scaled(
            self.image_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )

        self.image_label.setPixmap(scaled)