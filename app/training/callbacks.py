import tensorflow as tf

from app.config import SAVED_MODELS_DIR


def get_callbacks(model_name):

    checkpoint = tf.keras.callbacks.ModelCheckpoint(
        SAVED_MODELS_DIR / f"{model_name}.keras",
        monitor="val_loss",
        save_best_only=True,
        verbose=1,
    )

    early_stop = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=8,
        restore_best_weights=True,
        verbose=1,
    )

    reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=3,
        min_lr=1e-6,
        verbose=1,
    )

    return [
        checkpoint,
        early_stop,
        reduce_lr,
    ]