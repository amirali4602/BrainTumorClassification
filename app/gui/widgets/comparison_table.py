from pathlib import Path
import csv

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)

from app.config import RESULTS_DIR


class ComparisonTable(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel("Model Comparison")
        )

        self.table = QTableWidget()

        self.table.setAlternatingRowColors(True)

        self.table.setSortingEnabled(True)

        self.table.verticalHeader().hide()

        self.table.horizontalHeader().setStretchLastSection(True)

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(self.table)

        self.refresh()

    def refresh(self):

        csv_file = RESULTS_DIR / "model_comparison.csv"

        if not csv_file.exists():

            self.table.clear()

            self.table.setRowCount(0)

            self.table.setColumnCount(0)

            return

        with open(
            csv_file,
            newline="",
            encoding="utf-8",
        ) as f:

            rows = list(csv.reader(f))

        if not rows:
            return

        headers = rows[0]

        data = rows[1:]

        self.table.setColumnCount(len(headers))

        self.table.setHorizontalHeaderLabels(headers)

        self.table.setRowCount(len(data))

        for r, row in enumerate(data):

            for c, value in enumerate(row):

                self.table.setItem(
                    r,
                    c,
                    QTableWidgetItem(value),
                )