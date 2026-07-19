from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class PredictionPanel(QFrame):

    def __init__(self):
        super().__init__()

        self.setMinimumWidth(340)

        self.setStyleSheet("""
        QFrame{
            background:#2B2D42;
            border-radius:12px;
            border:1px solid #3B3D55;
        }

        QLabel#Title{
            font-size:18px;
            font-weight:bold;
            color:white;
            border:none;
        }

        QLabel#Header{
            font-size:12px;
            color:#BBBBBB;
            border:none;
        }

        QLabel#Value{
            font-size:16px;
            font-weight:bold;
            color:white;
            border:none;
        }
        """)

        layout = QVBoxLayout(self)

        layout.setSpacing(18)

        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("Prediction")

        title.setObjectName("Title")

        layout.addWidget(title)

        layout.addSpacing(10)

        layout.addWidget(QLabel("Model"))
        self.model_box = QComboBox()

        self.model_box.addItems(
            [
                "Custom CNN",
                "ResNet50",
                "EfficientNetB0",
            ]
        )

        layout.addWidget(self.model_box)

        layout.addSpacing(10)

        layout.addWidget(self._header("Prediction"))

        self.prediction_label = self._value("-")

        layout.addWidget(self.prediction_label)

        layout.addSpacing(10)

        layout.addWidget(self._header("Confidence"))

        self.confidence_label = self._value("-")

        layout.addWidget(self.confidence_label)

        layout.addSpacing(15)

        layout.addWidget(self._header("Class Probabilities"))

        self.probability_labels = {}

        for cls in (
            "Glioma",
            "Meningioma",
            "Pituitary",
            "No Tumor",
        ):

            label = QLabel(f"{cls:<15} 0.00 %")

            label.setObjectName("Value")

            self.probability_labels[cls] = label

            layout.addWidget(label)

        layout.addStretch()

        self.load_button = QPushButton("Load Image")

        self.predict_button = QPushButton("Predict")

        self.clear_button = QPushButton("Clear")

        layout.addWidget(self.load_button)

        layout.addWidget(self.predict_button)

        layout.addWidget(self.clear_button)

    def _header(self, text):

        label = QLabel(text)

        label.setObjectName("Header")

        return label

    def _value(self, text):

        label = QLabel(text)

        label.setObjectName("Value")

        return label