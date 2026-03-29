import streamlit as st
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('punkt')
nltk.download('stopwords')

st.title("🧹 Clean My Text")

text = st.text_area("Enter your text:")#Hiii, this is keerthi ,your GenAI trainer so i welcome you all to 2  the session!!
custom_stop_Words=st.text_area("enter your own stopwords (Comma-separated)")

lower = st.checkbox("Convert to lowercase")
remove_punct = st.checkbox("Remove punctuation")
remove_num = st.checkbox("Remove numbers")
remove_stop = st.checkbox("Remove stopwords")
remove_url_And_email =st.checkbox("Remove url and email")
# remove_email =st.checkbox("Remove Email")

if st.button("Clean Text"):
    result = text

    if lower:
        result = result.lower()

    if remove_punct:
        result = ''.join([ch for ch in result if ch not in string.punctuation])

    if remove_num:
        result = ''.join([ch for ch in result if not ch.isdigit()])

    if remove_stop:
        words = word_tokenize(result)
        result = ' '.join([word for word in words if word not in stopwords.words('english')and word not in custom_stop_Words.lower().split(',')])

    if remove_url_And_email:
        result = re.sub(r"http\S+|www\S+|[^a-zA-Z\s]|\S+@\S+\s",'',  result)


    # if remove_email:
    #     result=re.sub(r"\S+@\S+\s|[^a-zA-Z\s]",'',result)

    
    st.subheader("Cleaned Text:")
    st.write(result)

    # After cleaning
    words = result.split()
    st.write("Word Count:", len(words))

    freq = Counter(words)
    st.write("Top 4 Words:", freq.most_common(4))

