import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

st.title("Bag of Words Visualizer")

sentences = st.text_area("Enter sentences (one per line)").split("\n")

if st.button("Generate BoW"):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(sentences)
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    st.write(df)
    
   
