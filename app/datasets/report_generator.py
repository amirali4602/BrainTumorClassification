import pandas as pd

from app.config import RESULTS_DIR


class DatasetReport:

    OUTPUT = RESULTS_DIR / "dataset"

    def save_csv(self, distribution):

        df = pd.DataFrame(
            {
                "Class": list(distribution.keys()),
                "Images": list(distribution.values()),
            }
        )

        df.to_csv(
            self.OUTPUT / "dataset_summary.csv",
            index=False,
        )

    def save_markdown(
        self,
        distribution,
        avg_size,
        min_size,
        max_size,
    ):

        report = f"""# Dataset Report

## Class Distribution

{distribution}

## Average Size

{avg_size}

## Minimum Size

{min_size}

## Maximum Size

{max_size}
"""

        with open(
            self.OUTPUT / "dataset_report.md",
            "w",
            encoding="utf8",
        ) as f:

            f.write(report)