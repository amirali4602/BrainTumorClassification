from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


class MainToolBar(QToolBar):

    def __init__(self):
        super().__init__("Main Toolbar")

        self.setMovable(False)

        self.open_action = QAction("Open Image", self)
        self.predict_action = QAction("Predict", self)
        self.clear_action = QAction("Clear", self)
        self.exit_action = QAction("Exit", self)

        self.addAction(self.open_action)
        self.addSeparator()

        self.addAction(self.predict_action)
        self.addSeparator()

        self.addAction(self.clear_action)
        self.addSeparator()

        self.addAction(self.exit_action)