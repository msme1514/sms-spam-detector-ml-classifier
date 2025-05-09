import streamlit as st
from spam_predictor import SpamPredictor

# Load model and vectorizer
predictor = SpamPredictor(
    model_path="sms_spam_classifier_model.joblib",
    vectorizer_path="vectorizer.joblib"
)

# Streamlit UI
st.title("📩 SMS Spam Classifier")
st.write("Enter an SMS message below to check if it's Spam or Ham.")

user_input = st.text_area("Enter your message here:")

if st.button("Check"):
    if user_input.strip():
        result = predictor.predict(user_input)
        st.success(f"The message is classified as: **{result}**")
    else:
        st.warning("Please enter a message to classify.")
