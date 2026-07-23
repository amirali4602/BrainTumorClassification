from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QWidget,
    QProgressBar
)


class PredictionPanel(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        title = QLabel("Prediction")

        title.setAlignment(Qt.AlignCenter)

        self.progress_bars = {}

        classes = [
            "glioma",
            "meningioma",
            "notumor",
            "pituitary",
        ]

        for cls in classes:

            label = QLabel(cls.capitalize())

            bar = QProgressBar()

            bar.setRange(0, 100)

            bar.setValue(0)

            layout.addWidget(label)

            layout.addWidget(bar)

            self.progress_bars[cls] = bar

        self.model_label = QLabel("-")

        self.class_label = QLabel("-")

        self.confidence_label = QLabel("-")


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

        layout.addStretch()

    def update_result(
        self,
        result,
        model_name,
    ):

        self.model_label.setText(model_name)

        self.class_label.setText(
            result.predicted_class.capitalize()
        )

        self.confidence_label.setText(
            f"{result.confidence * 100:.2f}%"
        )

        for name, probability in result.probabilities.items():

            self.progress_bars[name].setValue(
                int(probability * 100)
            )

        for name, bar in self.progress_bars.items():

            if name == result.predicted_class:
                bar.setFormat(f"{bar.value()}% ✓")
            else:
                bar.setFormat(f"{bar.value()}%")

    def clear(self):

        self.class_label.setText("-")

        self.confidence_label.setText("-")

        for bar in self.progress_bars.values():

            bar.setValue(0)

            bar.setFormat("%p%")