from app.inference.predictor import Predictor


predictor = Predictor()

result = predictor.predict(
    "Dataset/Testing/glioma/Te-gl_0010.jpg",
    "Custom CNN",
)

print(result)