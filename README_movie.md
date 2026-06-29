# Movie Review Sentiment Analyzer





\# 🎬 Movie Review Sentiment Analyzer



\## Overview



Movie Review Sentiment Analyzer is a Natural Language Processing (NLP) based machine learning application that predicts whether a movie review expresses a positive or negative sentiment.



The application is built using Streamlit and allows users to enter a movie review in plain text. The review is processed using a pre-trained TF-IDF vectorizer and classified by a trained machine learning model.



\---



\## Problem Statement



People often share opinions about movies online through reviews. Analyzing thousands of reviews manually can be time-consuming. This project automates the sentiment classification process by determining whether a review is positive or negative.



\---



\## Features



\* Real-time sentiment prediction

\* User-friendly Streamlit interface

\* Positive and Negative classification

\* Sample review visualization

\* NLP text processing

\* Machine Learning based prediction



\---



\## Technologies Used



\* Python

\* Streamlit

\* Pandas

\* NLTK

\* Scikit-learn

\* Pickle



\---



\## Machine Learning Workflow



1\. Collect movie review dataset

2\. Clean and preprocess text

3\. Convert text into numerical features using TF-IDF

4\. Train sentiment classification model

5\. Save trained model and vectorizer

6\. Deploy using Streamlit



\---



\## Input



Users enter a movie review such as:



"The movie was amazing. The acting and story were excellent."



\---



\## Output



Positive Sentiment



or



Negative Sentiment



\---



\## Project Structure



Movie-Review-Sentiment-Analyzer/



├── app.py



├── sentiment movie.csv



├── model sentiment.pkl



├── tfv sentiment.pkl



├── requirements.txt



└── README.md



\---



\## Installation



```bash

pip install -r requirements.txt

```



\## Run Application



```bash

streamlit run app.py

```



\---



\## Required Files



\* app.py

\* sentiment movie.csv

\* model sentiment.pkl

\* tfv sentiment.pkl



\---



\## Future Improvements



\* Multi-class sentiment classification

\* Emotion detection

\* Confidence score display

\* Multi-language support

\* Cloud deployment



\---



\## Author



Developed using Machine Learning, NLP, and Streamlit.



