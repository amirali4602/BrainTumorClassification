import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from app.gui.styles.stylesheet import APP_STYLESHEET


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NeuroVision AI")

        self.resize(1400, 800)


def run():

    app = QApplication(sys.argv)

    app.setStyleSheet(APP_STYLESHEET)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())