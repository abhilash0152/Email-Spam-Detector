import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import streamlit as st 
import joblib

vectorizer = joblib.load('vectorizer.pkl')
model = joblib.load('model.pkl')
ps = PorterStemmer()

def text_encoder(mail):
    y=[]
    words = nltk.word_tokenize(mail.lower())
    for i in words:
        if i.isalnum():
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)
    return " ".join(y)
st.title('Email Spam Detector')  
user_input = st.text_area('Write the Mail')   
if st.button('Predict'):
        msg = text_encoder(user_input)
        vector = vectorizer.transform([msg])
        predict = model.predict(vector.toarray())[0]
        if predict==1:
            st.error("SPAM Alert!!")
        else:
            st.success("This looks safe.")