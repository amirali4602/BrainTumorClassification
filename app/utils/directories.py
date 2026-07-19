from app.config import (
    RESULTS_DIR,
    REPORTS_DIR,
    SAVED_MODELS_DIR,
    LOGS_DIR,
)


def create_directories() -> None:

    directories = [
        RESULTS_DIR,
        RESULTS_DIR / "dataset",
        REPORTS_DIR,
        SAVED_MODELS_DIR,
        LOGS_DIR,
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)