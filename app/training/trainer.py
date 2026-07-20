from app.config import EPOCHS

from app.training.callbacks import get_callbacks


class Trainer:

    def train(
        self,
        model,
        train_dataset,
        validation_dataset,
        model_name,
        epochs=EPOCHS,
    ):

        history = model.model.fit(
            train_dataset,
            validation_data=validation_dataset,
            epochs=epochs,
            callbacks=get_callbacks(model_name),
        )

        return history