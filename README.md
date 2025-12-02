
# 📧 Smart Email Sorter 

A simple ML project that automatically classifies emails into categories like
**Work, Shopping, Promotion, Spam, Finance, Travel, Social**, etc.

This project uses **TF-IDF + Logistic Regression**, built with **Python**, trained in Jupyter, and deployed on **Streamlit Cloud**.

## Features

* Classifies email text into predefined categories
* Clean and easy-to-use Streamlit UI
* Fast & lightweight ML model
* Beginner-friendly project
* Fully deployable with Streamlit Cloud


## Machine Learning Model

* **Vectorizer:** `TfidfVectorizer(stop_words='english')`
* **Classifier:** `LogisticRegression(max_iter=500)`
* **Accuracy Achieved:** ~73%
* Model files included:

  * `model.pkl`
  * `vectorizer.pkl`


## 📁 Project Structure

smart_email_sorter/
│── app.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md


##  How It Works

1. User enters an email text
2. Text is transformed using TF-IDF
3. Machine Learning model predicts the category
4. Result is displayed instantly in the UI


## Run Locally

Install the required libraries:
pip install -r requirements.txt

Run the app:
streamlit run app.py

## Live Demo

The project is deployed on Streamlit Cloud:

👉 **[https://smartemailsorter-wfzxgr7ngyrqxbevw2xbm4.streamlit.app/]**


## Technologies Used

* Python
* Scikit-learn
* Pandas
* Streamlit
* TF-IDF Vectorization
* Logistic Regression


