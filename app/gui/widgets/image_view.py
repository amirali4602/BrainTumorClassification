from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class ImageView(QWidget):

    imageDropped = Signal(str)

    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)

        self.set_default_style()

        self.current_pixmap = None

        layout = QVBoxLayout(self)

        self.image_label = QLabel(
            "🖼️\n\nDrop MRI Image Here\n\nor\n\nOpen Image (Ctrl+O)"
        )
        self.image_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.image_label)
        font = self.image_label.font()
        font.setPointSize(14)
        self.image_label.setFont(font)

        self.image_label.setStyleSheet(
            "color: #fff; border: none;"
            
        )

    def set_image(self, filename):
        self.current_pixmap = QPixmap(filename)
        self._update_pixmap()

    def clear(self):
        self.current_pixmap = None
        self.image_label.clear()
        self.image_label.setText(
            "🖼️\n\nDrop MRI Image Here\n\nor\n\nOpen Image (Ctrl+O)"
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

            self.set_drag_style()

            event.acceptProposedAction()

        else:

            event.ignore()
    def dragLeaveEvent(self, event):

        self.set_default_style()

        event.accept()
    def dropEvent(self, event):

        self.set_default_style()

        urls = event.mimeData().urls()

        if not urls:
            return

        filename = urls[0].toLocalFile()

        self.imageDropped.emit(filename)

        event.acceptProposedAction()

    def set_default_style(self):

        self.setStyleSheet("""
            background-color: #252526;
            border: 3px dashed #6b7280;
            border-radius: 12px;
        """)


    def set_drag_style(self):

        self.setStyleSheet("""
            background-color: #1e3a5f;
            border: 3px dashed #3daee9;
            border-radius: 12px;
        """)