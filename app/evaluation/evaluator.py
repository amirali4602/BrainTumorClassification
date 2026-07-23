import numpy as np

from sklearn.metrics import confusion_matrix

from app.evaluation.metrics import calculate_metrics
from app.evaluation.confusion import save_confusion_matrix
from app.evaluation.reports import save_report
from app.evaluation.predictions import save_predictions


class Evaluator:

    def evaluate(
        self,
        model,
        test_dataset,
        class_names,
        output,
    ):

        predictions = model.model.predict(
            test_dataset,
            verbose=0,
        )

        y_pred = np.argmax(
            predictions,
            axis=1,
        )


        y_true = np.concatenate(
            [
                labels.numpy()
                for _, labels in test_dataset
            ]
        )


        metrics = calculate_metrics(
            y_true,
            y_pred,
        )


        # Save confusion matrix values
        cm = confusion_matrix(
            y_true,
            y_pred,
        )

        np.save(
            output / "confusion_matrix.npy",
            cm,
        )


        save_confusion_matrix(
            y_true,
            y_pred,
            class_names,
            output,
        )


        save_predictions(
            y_true,
            y_pred,
            class_names,
            output,
        )


        save_report(
            metrics,
            output,
        )


        return metrics