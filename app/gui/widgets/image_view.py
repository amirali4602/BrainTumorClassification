from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class ImageView(QWidget):

    imageDropped = Signal(str)

    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)

        self.current_pixmap = None

        layout = QVBoxLayout(self)

        self.image_label = QLabel(
            "Drop MRI Image Here\n\nor\n\nClick Open Image"
        )
        self.image_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.image_label)

    def set_image(self, filename):
        self.current_pixmap = QPixmap(filename)
        self._update_pixmap()

    def clear(self):
        self.current_pixmap = None
        self.image_label.clear()
        self.image_label.setText(
            "Drop MRI Image Here\n\nor\n\nClick Open Image"
        )

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_pixmap()

    def _update_pixmap(self):
        if self.current_pixmap is None:
            return

        self.image_label.setPixmap(
            self.current_pixmap.scaled(
                self.image_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()

        if not urls:
            return

        filename = urls[0].toLocalFile()

        self.imageDropped.emit(filename)

        event.acceptProposedAction()