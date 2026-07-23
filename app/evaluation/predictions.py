import pandas as pd


def save_predictions(
    y_true,
    y_pred,
    class_names,
    output,
):

    df = pd.DataFrame({
        "Actual": [class_names[i] for i in y_true],
        "Predicted": [class_names[i] for i in y_pred],
        "Correct": y_true == y_pred,
    })

    df.to_csv(
        output / "predictions.csv",
        index=False,
    )