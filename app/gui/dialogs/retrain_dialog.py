from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QSpinBox,
)


class RetrainDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Retrain Model")

        layout = QFormLayout(self)

        self.model_box = QComboBox()

        self.model_box.addItems(
            [
                "Custom CNN",
                "ResNet50",
                "EfficientNetB0",
            ]
        )

        self.epochs = QSpinBox()

        self.epochs.setRange(1, 100)

        self.epochs.setValue(20)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok
            | QDialogButtonBox.Cancel
        )

        buttons.accepted.connect(self.accept)

        buttons.rejected.connect(self.reject)

        layout.addRow(
            "Model",
            self.model_box,
        )

        layout.addRow(
            "Epochs",
            self.epochs,
        )

        layout.addWidget(buttons)