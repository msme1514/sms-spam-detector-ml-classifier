# 📩 SMS Spam Classifier

This is a simple and interactive web app built using **Streamlit** that classifies SMS messages as **Spam** or **Ham** using a trained **Multinomial Naive Bayes** model.

---

## 🚀 Features

- 🔤 Enter any SMS message and instantly check if it's spam.
- 🧠 Uses CountVectorizer for text preprocessing.
- 🤖 Powered by Scikit-learn’s MultinomialNB classifier.
- 🖱️ Clean Streamlit interface with input form, result display, and reset button.
- ⚡ Fast, lightweight, and easy to deploy locally or on the cloud.

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```


## 🧠 Model Info

- **Algorithm**: Multinomial Naive Bayes (`MultinomialNB`)
- **Text Preprocessing**: `CountVectorizer` from Scikit-learn
- **Training Data**: SMS text labeled as `spam` or `ham`
- **Model Files**:
  - `sms_spam_classifier_model.joblib`: Trained Naive Bayes model
  - `vectorizer.joblib`: Fitted `CountVectorizer`
- **Input**: Raw text from user
- **Output**: Classification label: `"Spam"` or `"Ham"`
  
---
## Screenshots
![image](https://github.com/user-attachments/assets/30d52cbb-24a7-4202-8b10-8b305e4d4b7a)

---

## Notebook
https://colab.research.google.com/drive/1wSl00qLlK3qz2mx8ss7KBvd5DnJNSwJk?usp=sharing

##  🙌 Acknowledgments
Scikit-learn – For the machine learning tools.

Streamlit – For the web app framework.

Inspired by classic spam detection datasets and tutorials.
