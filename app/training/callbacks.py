import tensorflow as tf

from app.config import SAVED_MODELS_DIR


def get_callbacks(model_name):

    checkpoint = tf.keras.callbacks.ModelCheckpoint(
        SAVED_MODELS_DIR / f"{model_name}.keras",
        monitor="val_loss",
        save_best_only=True,
    )

    early_stop = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=5,
        restore_best_weights=True,
    )

    reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=2,
    )

    return [
        checkpoint,
        early_stop,
        reduce_lr,
    ]