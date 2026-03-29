# Enhance your Streamlit app to:
# Show POS tag from spaCy for each word
# Highlight if spaCy’s lemma is different from the original word
import streamlit as st
import nltk
import spacy
from nltk.corpus import stopwords 
# Download resources
nltk.download('punkt')
nltk.download('stopwords')
# Load spaCy

nlp = spacy.load("en_core_web_sm")
st.title("🔁 Lemmatization with POS (spaCy)")
text = st.text_input("Enter a sentence:")
remove_stop = st.checkbox("Remove stopwords")


if st.button("Process"):
    if remove_stop:
        filtered_text=' '.join([word for word in text.split() if word not in stopwords.words("english")])
        text=filtered_text
    doc = nlp(text)
    # print(doc)
    # print(type(doc))
    st.markdown("### Results:")
    for token in doc:
        pos = token.pos_   # Part of Speech
        original = token.text  # Token
        lemma = token.lemma_  # lamatization
        # Ignore case differences for comparison
        if pos == "PROPN":  # Proper nouns usually don't change
            highlight = '<span style="color:yellow;">(Proper Noun - Same)</span>'
        elif original.lower() != lemma.lower():
            highlight = '<span style="color:green;">(Changed)</span>'
        else:
            highlight = '<span style="color:red;">(Same)</span>'

        st.markdown(f"**{original}** ({pos}) → **{lemma}** {highlight}", unsafe_allow_html=True)
