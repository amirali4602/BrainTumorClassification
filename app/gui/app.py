import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QWidget,
)

from app.gui.styles.stylesheet import APP_STYLESHEET
from app.gui.widgets.image_view import ImageView


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NeuroVision AI")

        self.resize(1400, 800)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        layout.setContentsMargins(15, 15, 15, 15)

        self.image_view = ImageView()

        layout.addWidget(
            self.image_view,
            stretch=2,
        )
        

def run():

    app = QApplication(sys.argv)

    app.setStyleSheet(APP_STYLESHEET)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())