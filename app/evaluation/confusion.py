import matplotlib.pyplot as plt

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix


def save_confusion_matrix(
    y_true,
    y_pred,
    class_names,
    output,
):

    cm = confusion_matrix(
        y_true,
        y_pred,
    )

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_title("Confusion Matrix")
    ConfusionMatrixDisplay(
        cm,
        display_labels=class_names,
    ).plot(
        cmap="Blues",
        values_format="d",
        xticks_rotation=20,
        colorbar=False,
        ax=ax,
    )

    plt.tight_layout()

    plt.savefig(
        output / "confusion_matrix.png",
        dpi=300,
    )

    plt.close(fig)