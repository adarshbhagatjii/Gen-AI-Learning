# Sentace tokenizer using NLTK and displayed using streamlit

import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import pandas as pd
nltk.download('punkt')
nltk.download('pun_tab')
st.title("Sentence Tokenizer")
text=st.text_area("enter some text:")

if st.button("tokenize"):
    tokens_nltk=word_tokenize(text)
    # tokens_nltk_sent=sent_tokenize(text)
    # import spacy 
    # nlp=spacy.load("en_core_web_sm")
    # doc=nlp(text)
    # sent_token_spacy=[token.text for token in doc.sents]

    

    # st.write("sent_tokens by NLTK : ", tokens_nltk_sent)
    # st.write("sent_tokens by NLTK : ", len(tokens_nltk_sent))
    # st.write("First sent_token by NLTK : ", tokens_nltk_sent[0])
    # st.write("Last sent_token NLTK : ", (tokens_nltk_sent[-1]))

    
    # st.write("sent_tokens by SPACY : ", sent_token_spacy)
    # st.write("sent_tokens by SPACY : ", len(sent_token_spacy))
    # st.write("First sent_token by SPACY : ", sent_token_spacy[0])
    # st.write("Last sent_token SPACY : ", (sent_token_spacy[-1]))


    from nltk.corpus import stopwords 
    nltk.download('stopwords')
    filtered=[word for word in tokens_nltk if word not in stopwords.words("english")]
    st.write("nltk_tokens by NLTK : ", tokens_nltk)

    st.write("Cleaned tokens after removing stopwords : ", filtered)
    st.write("Count of removed Stopwords ", (len(tokens_nltk)-len(filtered)))


    # Task 3-----
    from collections import Counter
    token_freq=Counter(filtered)
    st.bar_chart(token_freq.most_common(5))

    # Task 4. -----

    st.write("count of words left after cleaning : ", len(filtered))
    st.write("3 most frequent word after clening : ", token_freq.most_common(3))
    

