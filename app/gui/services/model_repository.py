import json

from app.config import RESULTS_DIR


class ModelRepository:

    def load_models(self):

        models = []

        if not RESULTS_DIR.exists():
            return models

        for folder in RESULTS_DIR.iterdir():

            if not folder.is_dir():
                continue

            report = folder / "metrics.json"

            if not report.exists():
                continue

            with open(report, encoding="utf-8") as f:
                metrics = json.load(f)

            models.append({
                "name": folder.name,
                "accuracy": metrics.get("accuracy", 0),
                "precision": metrics.get("precision", 0),
                "recall": metrics.get("recall", 0),
                "f1": (
                    metrics.get("f1_score")
                    or metrics.get("f1")
                    or 0
                ),
            })

        return models