from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class PredictionPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Prediction")

        title.setAlignment(Qt.AlignCenter)

        self.model_label = QLabel("-")

        self.class_label = QLabel("-")

        self.confidence_label = QLabel("-")

        self.table = QTableWidget(4, 2)

        self.table.setHorizontalHeaderLabels(
            [
                "Class",
                "Probability",
            ]
        )

        self.table.verticalHeader().hide()

        self.table.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(title)

        layout.addWidget(QLabel("Model"))

        layout.addWidget(self.model_label)

        layout.addWidget(QLabel("Prediction"))

        layout.addWidget(self.class_label)

        layout.addWidget(QLabel("Confidence"))

        layout.addWidget(self.confidence_label)

        line = QFrame()

        line.setFrameShape(QFrame.HLine)

        layout.addWidget(line)

        layout.addWidget(QLabel("Probabilities"))

        layout.addWidget(self.table)

        layout.addStretch()

    def update_result(self, result, model_name):

        self.model_label.setText(model_name)

        self.class_label.setText(
            result.predicted_class
        )

        self.confidence_label.setText(
            f"{result.confidence * 100:.2f}%"
        )

        for row, (name, value) in enumerate(
            result.probabilities.items()
        ):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(name),
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    f"{value * 100:.2f}%"
                ),
            )

    def clear(self):

        self.model_label.setText("-")

        self.class_label.setText("-")

        self.confidence_label.setText("-")

        self.table.clearContents()