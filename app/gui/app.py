import sys

from PySide6.QtWidgets import QApplication


from app.gui.styles.stylesheet import APP_STYLESHEET
from app.gui.windows.main_window import MainWindow


def run():

    app = QApplication(sys.argv)

    app.setStyleSheet(APP_STYLESHEET)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())