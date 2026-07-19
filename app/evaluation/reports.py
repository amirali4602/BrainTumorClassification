import json
import pandas as pd


def save_report(metrics, output):

    with open(
        output / "metrics.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(metrics, f, indent=4)

    report_df = pd.DataFrame(
        metrics["classification_report"]
    ).transpose()

    report_df.to_csv(
        output / "classification_report.csv"
    )

    with open(
        output / "evaluation.md",
        "w",
        encoding="utf-8",
    ) as f:

        f.write("# Model Evaluation\n\n")

        f.write(f"Accuracy : {metrics['accuracy']:.4f}\n\n")
        f.write(f"Precision: {metrics['precision']:.4f}\n\n")
        f.write(f"Recall   : {metrics['recall']:.4f}\n\n")
        f.write(f"F1 Score : {metrics['f1']:.4f}\n")