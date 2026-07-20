from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
)


class ModelsTable(QTableWidget):

    HEADERS = [
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1",
        "Status",
    ]

    def __init__(self):
        super().__init__(0, len(self.HEADERS))

        self.setHorizontalHeaderLabels(self.HEADERS)

        self.horizontalHeader().setStretchLastSection(True)

        self.verticalHeader().hide()

    def add_model(
        self,
        name,
        accuracy,
        precision,
        recall,
        f1,
        status="Available",
    ):

        row = self.rowCount()

        self.insertRow(row)

        values = [
            name,
            f"{accuracy:.2%}",
            f"{precision:.2%}",
            f"{recall:.2%}",
            f"{f1:.2%}",
            status,
        ]

        for column, value in enumerate(values):

            self.setItem(
                row,
                column,
                QTableWidgetItem(str(value)),
            )
    def clear_models(self):

        self.setRowCount(0)


    def load_models(self, models):

        self.clear_models()

        for model in models:

            self.add_model(
                model["name"],
                model["accuracy"],
                model["precision"],
                model["recall"],
                model["f1"],
            )

    def selected_model(self):

        row = self.currentRow()

        if row < 0:
            return None

        item = self.item(row, 0)

        if item is None:
            return None

        return item.text()