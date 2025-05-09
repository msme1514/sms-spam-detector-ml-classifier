# 📩 SMS Spam Classifier

A simple web app built with Streamlit that classifies SMS messages as **Spam** or **Ham** using a trained `Multinomial Naive Bayes` model.

---

## 🚀 Features

- Input any SMS text and get an instant classification.
- Built using Scikit-learn for machine learning.
- `CountVectorizer` for text preprocessing.
- Lightweight and interactive UI powered by Streamlit.

---

## 📦 Requirements

Install required Python packages using:

```bash
pip install -r requirements.txt

---

## Project Structure
├── app.py                      # Streamlit frontend
├── spam_predictor.py          # Prediction helper class
├── vectorizer.joblib          # Saved CountVectorizer
├── sms_spam_classifier_model.joblib  # Trained MultinomialNB model
├── README.md                  # Project overview
└── requirements.txt           # Python dependencies

---
🧠 Model Info
Trained using Scikit-learn's MultinomialNB.

Preprocessing via CountVectorizer.

Saved using joblib for efficient reuse.
