import joblib

class SpamPredictor:
    def __init__(self, model_path: str, vectorizer_path: str):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def predict(self, text: str) -> str:
        # Transform text into vector
        text_vector = self.vectorizer.transform([text])
        # Predict using the model
        prediction = self.model.predict(text_vector)
        # Return the prediction result
        return "Spam" if prediction[0] == "spam" else "Ham"
