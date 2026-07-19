from app.config import MODEL_NAME
from app.training.runner import TrainingRunner
from app.models.registry import get_model





def main():

    model = get_model(MODEL_NAME)

    TrainingRunner(
        model,
        MODEL_NAME,
    ).run()


if __name__ == "__main__":
    main()