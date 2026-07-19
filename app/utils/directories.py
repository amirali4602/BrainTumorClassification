from app.config import (
    RESULTS_DIR,
    REPORTS_DIR,
    SAVED_MODELS_DIR,
    LOGS_DIR,
)


def create_directories() -> None:

    for directory in (
        RESULTS_DIR,
        REPORTS_DIR,
        SAVED_MODELS_DIR,
        LOGS_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)