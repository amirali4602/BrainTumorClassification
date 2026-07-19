from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
)
from PySide6.QtGui import QAction
from app.gui.styles.stylesheet import APP_STYLESHEET
from app.gui.widgets.image_view import ImageView
from app.gui.widgets.prediction_panel import PredictionPanel
from app.gui.widgets.toolbar import MainToolBar

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

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