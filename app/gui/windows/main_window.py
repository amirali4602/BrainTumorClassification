from pathlib import Path
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QDialog,
    QDockWidget
)
from PySide6.QtGui import QAction, QIcon, Qt
from app.config import LOGO_DIR, VALID_EXTENSIONS
from app.gui.widgets.log_console import LogConsole
from app.gui.widgets.toolbar import MainToolBar
from app.gui.dialogs.file_dialog import open_image_dialog
from app.inference.predictor import Predictor
from app.gui.dialogs.about_dialog import show_about
from app.gui.dialogs.retrain_dialog import RetrainDialog
from app.training.retrainer import ModelRetrainer

from PySide6.QtWidgets import QTabWidget
from app.gui.pages.prediction_page import PredictionPage
from app.gui.pages.analytics_page import AnalyticsPage
from app.gui.pages.models_page import ModelsPage

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.current_image = None
        self.current_model = "Custom CNN"
        self.predictor = Predictor()
        self.log_console = LogConsole()
        self._initialize_window()

        self._create_central_widget()
        self._create_menu_bar()
        self._create_tool_bar()
        self._create_status_bar()

        self._connect_signals()


        dock = QDockWidget("Log", self)

        dock.setWidget(self.log_console)

        self.addDockWidget(
            Qt.BottomDockWidgetArea,
            dock,
        )

    def _initialize_window(self):
        
        self.setWindowTitle("NeuroVision AI")
        self.resize(1400, 800)
        self.setMinimumSize(1200, 700)
        self.setWindowIcon(QIcon(LOGO_DIR))

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
        self.prediction_page.image_view.imageDropped.connect(
            self.load_image
        )
        self.about_action.triggered.connect(
            lambda: show_about(self)
        )
        self.toolbar.retrain_action.triggered.connect(
            self.retrain_model
        )
        self.models_page.activate_button.clicked.connect(
            self.activate_selected_model
        )
    def _create_central_widget(self):

        self.tabs = QTabWidget()

        self.prediction_page = PredictionPage()

        self.analytics_page = AnalyticsPage()

        self.models_page = ModelsPage()

        self.tabs.addTab(
            self.prediction_page,
            "Prediction",
        )

        self.tabs.addTab(
            self.analytics_page,
            "Analytics",
        )

        self.tabs.addTab(
            self.models_page,
            "Models",
        )

        self.setCentralWidget(self.tabs)

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

        self.open_action.setShortcut("Ctrl+O")

        self.exit_action.setShortcut("Ctrl+Q")

        self.custom_action.setShortcut("Ctrl+1")

        self.resnet_action.setShortcut("Ctrl+2")

        self.efficient_action.setShortcut("Ctrl+3")


    def _create_tool_bar(self):

        self.toolbar = MainToolBar()

        self.addToolBar(self.toolbar)

        self.toolbar.predict_action.setShortcut("Ctrl+P")

        self.toolbar.clear_action.setShortcut("Ctrl+L")

    def _create_status_bar(self):

        self.status_bar = self.statusBar()

        self.status_bar.showMessage("Ready")

        self.log_console.log("Image cleared.")

        self.model_status = QLabel()

        self.status_bar.addPermanentWidget(
            self.model_status
        )

        self.update_model_status()

    def update_model_status(self):

        self.model_status.setText(
            f"Model: {self.current_model}"
        )

    def open_image(self):

        filename = open_image_dialog(self)

        if filename:

            self.load_image(filename)
            
    def load_image(self, filename):
        suffix = Path(filename).suffix.lower()

        if suffix not in VALID_EXTENSIONS:

            self.status_bar.showMessage(
                "Unsupported file type."
            )

            return
        self.current_image = filename

        self.prediction_page.image_view.set_image(filename)

        self.status_bar.showMessage(
            f"Loaded: {Path(filename).name}"
        )
        self.log_console.log(
            f"Loaded image: {Path(filename).name}"
        )
        self.setWindowTitle(
            f"NeuroVision AI — {Path(filename).name}"
        )

    def predict_image(self):

        if self.current_image is None:
            return

        try:

            result = self.predictor.predict(
                self.current_image
            )

            self.prediction_page.prediction_panel.update_result(
                result,
                self.current_model,
            )
            self.status_bar.showMessage(
                "Prediction completed."
            )
            self.log_console.log(
                "Prediction completed."
            )

        except Exception as e:

            self.status_bar.showMessage(
                "Prediction failed."
            )
            self.log_console.log(
                "Prediction failed."
            )
            self.log_console.log(str(e))

    def change_model(self, name):

        self.current_model = name

        self.predictor.reload(name)
        folder_name = {
            "Custom CNN": "custom_cnn",
            "ResNet50": "resnet50",
            "EfficientNetB0": "efficientnetb0",
        }

        self.analytics_page.model_box.setCurrentText(
            folder_name[name]
        )

        self.analytics_page.load_results()

        self.update_model_status()

        self.status_bar.showMessage(
            f"Current model changed to {name}",
            3000,
        )
        self.log_console.log(
            f"Current model: {name}"
        )

    def clear_image(self):

        self.current_image = None

        self.prediction_page.image_view.clear()

        self.prediction_page.prediction_panel.clear()

        self.statusBar().showMessage(
            "Ready"
        )
        self.setWindowTitle("NeuroVision AI")

    def retrain_model(self):

        dialog = RetrainDialog(self)

        if dialog.exec() != QDialog.Accepted:
            return

        model = dialog.model_box.currentText()

        epochs = dialog.epochs.value()

        self.status_bar.showMessage(
            "Training started..."
        )
        self.log_console.log(
            "Training started..."
        )
        retrainer = ModelRetrainer()

        retrainer.train(
            model,
            epochs,
        )

        self.predictor.reload(model)

        self.change_model(model)

        self.status_bar.showMessage(
            "Training completed.",
            5000,
        )

        self.models_page.refresh()

        self.analytics_page.load_results()

    def activate_selected_model(self):

        model = self.models_page.table.selected_model()

        if model is None:

            self.status_bar.showMessage(
                "No model selected."
            )

            return

        names = {
            "custom_cnn": "Custom CNN",
            "resnet50": "ResNet50",
            "efficientnetb0": "EfficientNetB0",
        }

        self.change_model(
            names.get(model, model)
        )