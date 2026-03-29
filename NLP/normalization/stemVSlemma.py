import streamlit as st
import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import spacy
import pandas as pd

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
ps=PorterStemmer()
ls=LancasterStemmer()
lemmatizer= WordNetLemmatizer()
nlp=spacy.load('en_core_web_sm')
st.title("🔁 Stemming vs Lemmatization")
text=st.text_input("Enter a sentance or list of words: -")


if st.button("Process"):
    words=nltk.word_tokenize(text)
    results=[]
    for word in words:
        doc=nlp(word)
        spacy_lemma=doc[0].lemma_
        results.append({
            'Word':word,
            "PorterStemmer":ps.stem(word),
            "lancaster stem":ls.stem(word),
            "lemma (mltk)":lemmatizer.lemmatize(word),
            "Lemma (spacy)":spacy_lemma
        })

    df=pd.DataFrame(results)
    st.markdown("### Results Table")
    st.table(df)