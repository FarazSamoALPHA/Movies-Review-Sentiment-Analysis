import pandas as pd
import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords once
nltk.download('stopwords')

# Load stop words
stop_words = set(stopwords.words('english'))


# Streamlit UI
st.title('🎬 Movie Review Sentiment Analyzer')

# Load model and TF-IDF vectorizer
df=pd.read_csv("sentiment movie.csv")
model = pickle.load(open('model sentiment.pkl', 'rb'))
vectorizer = pickle.load(open('tfv sentiment.pkl', 'rb'))


# Optional: Show a few sample reviews
if st.checkbox("Show sample reviews"):
    df = pd.read_csv("sentiment movie.csv")
    st.write(df.sample(5))

# User input
user_input = st.text_area('📝 Write or Paste Movie Review Here', height=200)

# Predict button
if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text for analysis.")
    else:
        # Transform the input using loaded vectorizer
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]

        # Display result
        if prediction == 1:
            st.success("✅ The review sentiment is **Positive**.")
        else:
            st.error("❌ The review sentiment is **Negative**.")
