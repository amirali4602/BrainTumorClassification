from app.inference.predictor import Predictor


predictor = Predictor("ResNet50")

result = predictor.predict(
    "Dataset/Testing/glioma/Te-gl_0010.jpg"
)

print(result)