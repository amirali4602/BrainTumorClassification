from pathlib import Path
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
)
from PySide6.QtGui import QAction
from app.gui.widgets.image_view import ImageView
from app.gui.widgets.prediction_panel import PredictionPanel
from app.gui.widgets.toolbar import MainToolBar
from app.gui.dialogs.file_dialog import open_image_dialog
from app.inference.predictor import Predictor

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.current_image = None
        self.current_model = "Custom CNN"
        self.predictor = Predictor()

        self._initialize_window()

        self._create_central_widget()
        self._create_menu_bar()
        self._create_tool_bar()
        self._create_status_bar()

        self._connect_signals()

    def _initialize_window(self):
        
        self.setWindowTitle("NeuroVision AI")
        self.resize(1400, 800)
        self.setMinimumSize(1200, 700)

    def _connect_signals(self):

        self.exit_action.triggered.connect(self.close)
        self.toolbar.exit_action.triggered.connect(self.close)

        self.open_action.triggered.connect(self.open_image)
        self.toolbar.open_action.triggered.connect(self.open_image)

        self.toolbar.predict_action.triggered.connect(self.predict_image)
        self.toolbar.clear_action.triggered.connect(self.clear_image)

        self.custom_action.triggered.connect(
            lambda: self.change_model("Custom CNN")
        )

        self.resnet_action.triggered.connect(
            lambda: self.change_model("ResNet50")
        )

        self.efficient_action.triggered.connect(
            lambda: self.change_model("EfficientNetB0")
        )
    def _create_central_widget(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        layout.setContentsMargins(15, 15, 15, 15)

        self.image_view = ImageView()

        self.prediction_panel = PredictionPanel()

        layout.addWidget(self.image_view, 3)

        layout.addWidget(self.prediction_panel, 1)

    def _create_menu_bar(self):

        menubar = self.menuBar()

        file_menu = menubar.addMenu("&File")

        self.open_action = QAction("Open Image", self)

        self.exit_action = QAction("Exit", self)

        file_menu.addAction(self.open_action)

        file_menu.addSeparator()

        file_menu.addAction(self.exit_action)

        model_menu = menubar.addMenu("&Models")

        self.custom_action = QAction("Custom CNN", self)

        self.resnet_action = QAction("ResNet50", self)

        self.efficient_action = QAction("EfficientNetB0", self)

        model_menu.addActions([
            self.custom_action,
            self.resnet_action,
            self.efficient_action,
        ])

        help_menu = menubar.addMenu("&Help")

        self.about_action = QAction("About", self)

        help_menu.addAction(self.about_action)


    def _create_tool_bar(self):

        self.toolbar = MainToolBar()

        self.addToolBar(self.toolbar)


    def _create_status_bar(self):

        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")

    def open_image(self):

        filename = open_image_dialog(self)

        if not filename:
            return

        self.current_image = filename

        self.image_view.set_image(filename)

        self.status_bar.showMessage(
            f"Loaded: {Path(filename).name}"
        )

    def predict_image(self):

        if self.current_image is None:
            return

        try:

            result = self.predictor.predict(
                self.current_image,
                self.current_model,
            )

            self.prediction_panel.update_result(
                result,
                self.current_model,
            )
            self.status_bar.showMessage(
                "Prediction completed."
            )

        except Exception as e:

            self.status_bar.showMessage(
                "Prediction failed."
            )

            print(e)

    def change_model(self, name):

        self.current_model = name

        self.statusBar().showMessage(
            f"Model: {name}"
        )

    def clear_image(self):

        self.current_image = None

        self.image_view.clear()

        self.prediction_panel.clear()

        self.statusBar().showMessage(
            "Ready"
        )

