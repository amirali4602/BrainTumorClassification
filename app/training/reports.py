from pathlib import Path


def save_training_report(history, output_dir: Path):

    output_dir.mkdir(parents=True, exist_ok=True)

    final_epoch = len(history.history["accuracy"]) - 1

    report = f"""# Custom CNN Training Report

Final Training Accuracy:
{history.history["accuracy"][final_epoch]:.4f}

Final Validation Accuracy:
{history.history["val_accuracy"][final_epoch]:.4f}

Final Training Loss:
{history.history["loss"][final_epoch]:.4f}

Final Validation Loss:
{history.history["val_loss"][final_epoch]:.4f}

Epochs:
{len(history.history["accuracy"])}
"""

    with open(
        output_dir / "training_report.md",
        "w",
        encoding="utf8",
    ) as f:

        f.write(report)