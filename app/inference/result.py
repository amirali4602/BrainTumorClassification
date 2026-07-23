from dataclasses import dataclass


@dataclass
class PredictionResult:

    predicted_class: str

    confidence: float

    probabilities: dict[str, float]