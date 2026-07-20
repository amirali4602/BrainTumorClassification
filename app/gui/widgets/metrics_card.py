from PySide6.QtWidgets import (
    QFormLayout,
    QLabel,
    QGroupBox,
)


class MetricsCard(QGroupBox):

    def __init__(self):
        super().__init__("Model Metrics")

        layout = QFormLayout(self)

        self.accuracy = QLabel("-")
        self.precision = QLabel("-")
        self.recall = QLabel("-")
        self.f1 = QLabel("-")

        layout.addRow("Accuracy", self.accuracy)
        layout.addRow("Precision", self.precision)
        layout.addRow("Recall", self.recall)
        layout.addRow("F1 Score", self.f1)

    def clear(self):

        self.accuracy.setText("-")
        self.precision.setText("-")
        self.recall.setText("-")
        self.f1.setText("-")

    def update_metrics(self, metrics):

        self.accuracy.setText(
            f"{metrics.get('accuracy', 0):.2%}"
        )

        self.precision.setText(
            f"{metrics.get('precision', 0):.2%}"
        )

        self.recall.setText(
            f"{metrics.get('recall', 0):.2%}"
        )

        f1 = (
            metrics.get("f1_score")
            or metrics.get("f1")
            or 0
        )

        self.f1.setText(f"{f1:.2%}")