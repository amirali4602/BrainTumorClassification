# Architecture

```
Dataset
        │
        ▼
Preprocessing
        │
        ▼
Training
        │
        ▼
Evaluation
        │
        ▼
Inference
        │
        ▼
Desktop GUI
```

## Modules

### datasets

Responsible for loading and validating the dataset.

### preprocessing

Image preprocessing and augmentation.

### models

Neural network architectures.

### training

Training loops.

### evaluation

Metrics, confusion matrices and reports.

### inference

Single image prediction.

### gui

Desktop application built with PySide6.