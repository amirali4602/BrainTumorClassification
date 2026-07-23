from app.config import (
    IMAGE_HEIGHT,
    IMAGE_WIDTH,
    CHANNELS,
    NUM_CLASSES,
    RESULTS_DIR,
)

from app.preprocessing.loaders import DatasetLoader
from app.preprocessing.pipelines import (
    prepare_train,
    prepare_validation,
    prepare_test,
)

from app.training.trainer import Trainer
from app.training.history import HistoryManager
from app.training.reports import save_training_report
from app.evaluation.evaluator import Evaluator


class TrainingRunner:

    def __init__(
        self,
        model,
        model_name,
        epochs,
    ):

        self.model = model
        self.model_name = model_name
        self.epochs = epochs

    def run(self):

        loader = DatasetLoader()

        train_ds, val_ds, test_ds = loader.load()

        class_names = train_ds.class_names

        train_ds = prepare_train(
            train_ds,
            self.model_name,
        )

        val_ds = prepare_validation(
            val_ds,
            self.model_name,
        )

        test_ds = prepare_test(
            test_ds,
            self.model_name,
        )

        self.model.build(
            (
                IMAGE_HEIGHT,
                IMAGE_WIDTH,
                CHANNELS,
            ),
            NUM_CLASSES,
        )

        self.model.compile()

        output = RESULTS_DIR / self.model_name
        output.mkdir(parents=True, exist_ok=True)

        with open(
            output / "model_summary.txt",
            "w",
            encoding="utf-8",
        ) as f:
            self.model.model.summary(
                print_fn=lambda line: f.write(line + "\n")
            )

        trainer = Trainer()

        history = trainer.train(
            self.model,
            train_ds,
            val_ds,
            model_name=self.model_name,
            epochs=self.epochs,
        )

        HistoryManager(
            history,
            output,
        ).save_all()

        save_training_report(
            history,
            output,
        )

        Evaluator().evaluate(
            self.model,
            test_ds,
            class_names,
            output,
        )