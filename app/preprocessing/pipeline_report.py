from app.config import (
    IMAGE_SIZE,
    BATCH_SIZE,
    VALIDATION_SPLIT,
    SHUFFLE_BUFFER,
)

from app.config import RESULTS_DIR


def save_pipeline_report():

    report = f"""# Data Pipeline

## Image Size

{IMAGE_SIZE}

## Batch Size

{BATCH_SIZE}

## Validation Split

{VALIDATION_SPLIT}

## Shuffle Buffer

{SHUFFLE_BUFFER}

## Preprocessing

- Resize
- Normalize

## Augmentations

- Random Flip
- Random Rotation
- Random Zoom
- Random Contrast

## Optimizations

- Cache
- Prefetch
"""

    output = RESULTS_DIR / "dataset"

    output.mkdir(parents=True, exist_ok=True)

    with open(
        output / "pipeline.md",
        "w",
        encoding="utf8",
    ) as file:

        file.write(report)