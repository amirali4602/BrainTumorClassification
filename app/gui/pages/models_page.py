from PySide6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QWidget,
)

from app.gui.widgets.models_table import ModelsTable
from app.gui.services.model_repository import ModelRepository

class ModelsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.table = ModelsTable()

        self.activate_button = QPushButton(
            "Set Active Model"
        )

        layout.addWidget(self.table)

        layout.addWidget(self.activate_button)

        self.repository = ModelRepository()

        self.refresh()
        
    def refresh(self):

        models = self.repository.load_models()

        self.table.load_models(models)