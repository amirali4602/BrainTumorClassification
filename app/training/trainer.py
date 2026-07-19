from app.config import EPOCHS
from app.training.callbacks import get_callbacks


class Trainer:

    def train(
        self,
        model,
        train_dataset,
        validation_dataset,
        model_name,
    ):

        history = model.model.fit(
            train_dataset,
            validation_data=validation_dataset,
            epochs=EPOCHS,
            callbacks=get_callbacks(model_name),
            verbose=1,
        )

        return history