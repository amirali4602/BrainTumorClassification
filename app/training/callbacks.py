import tensorflow as tf

from app.config import SAVED_MODELS_DIR


def get_callbacks():

    checkpoint = tf.keras.callbacks.ModelCheckpoint(
        filepath=SAVED_MODELS_DIR / "custom_cnn.keras",
        save_best_only=True,
        monitor="val_accuracy",
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