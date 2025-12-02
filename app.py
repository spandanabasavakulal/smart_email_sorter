import streamlit as st
import pickle

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.title("📧 Smart Email Sorter")

email_text = st.text_area("Enter your email text:")

if st.button("Classify"):
    if email_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        text_vec = vectorizer.transform([email_text])
        prediction = model.predict(text_vec)[0]
        st.success(f"Predicted Category: **{prediction}**")
