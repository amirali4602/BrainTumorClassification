from app.config import (
    IMAGE_HEIGHT,
    IMAGE_WIDTH,
    CHANNELS,
    NUM_CLASSES,
)
from pathlib import Path

from app.config import RESULTS_DIR
from app.models.custom_cnn import CustomCNNModel

from app.preprocessing.loaders import DatasetLoader
from app.preprocessing.pipelines import (
    prepare_train,
    prepare_validation,
)

from app.training.trainer import Trainer
from app.config import RESULTS_DIR
from app.training.history import HistoryManager
from app.training.reports import save_training_report

def main():

    loader = DatasetLoader()

    train_ds, val_ds, _ = loader.load()

    train_ds = prepare_train(train_ds)

    val_ds = prepare_validation(val_ds)

    model = CustomCNNModel()

    model.build(
        (
            IMAGE_HEIGHT,
            IMAGE_WIDTH,
            CHANNELS,
        ),
        NUM_CLASSES,
    )

    model.compile()

    model.summary()
    summary_path = RESULTS_DIR / "custom_cnn"

    summary_path.mkdir(parents=True, exist_ok=True)

    with open(
        summary_path / "model_summary.txt",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(f"Model Name: {model.model.name}\n")
        f.write("=" * 60 + "\n\n")

        model.model.summary(print_fn=lambda line: f.write(line + "\n"))
    trainer = Trainer()

    history = trainer.train(
        model,
        train_ds,
        val_ds,
    )
    output = RESULTS_DIR / "custom_cnn"

    HistoryManager(
        history,
        output,
    ).save_all()

    save_training_report(
        history,
        output,
    )

if __name__ == "__main__":
    main()