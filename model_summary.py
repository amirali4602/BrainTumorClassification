from tensorflow.keras.models import load_model

model = load_model("saved_models/resnet50.keras")

model.summary()