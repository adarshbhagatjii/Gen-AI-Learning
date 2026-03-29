import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import nltk
import pandas as pd
nltk.download('punkt')
nltk.download('pun_tab')
st.title("Text Tokenizer")
text=st.text_area("enter some text:")

if st.button("tokenize"):
    tokens_nltk=word_tokenize(text)
    tokens_nltk_sent=sent_tokenize(text)
  
    import spacy 
    nlp=spacy.load("en_core_web_sm") 
    doc=nlp(text)
    sent_token_spacy=[token.text for token in doc.sents]
    tokens_spacy=[token.text for token in doc]

    st.write("sent_tokens by NLTK : ", tokens_nltk_sent)
    st.write("sent_tokens by NLTK : ", len(tokens_nltk_sent))
    st.write("First sent_token by NLTK : ", tokens_nltk_sent[0])
    st.write("Last sent_token NLTK : ", (tokens_nltk_sent[-1]))

    st.write("No of Tokens from NLTK:",len(tokens_nltk))
    st.write(" Tokens By NLTK :",tokens_nltk)
    st.write("No of Tokens BY SPACY :",len(tokens_spacy))
    st.write("Tokens By spacy:",tokens_spacy)
    
   
     
    token_freq_nltk=Counter(tokens_nltk)
    token_freq_spacy=Counter(tokens_spacy)

    st.write("Most frequency token by NLTK:",token_freq_nltk.most_common(3))
    st.write("token_freq_NLTK:",token_freq_nltk)

    st.write("Most frequency token by SPACY:",token_freq_spacy.most_common(3))
    st.write("token_freq_SPACY:",token_freq_spacy)



    ##displaying token freq in table 
    st.write("Token freq table")
    st.table(token_freq_nltk.items())
    st.table(token_freq_spacy.items())
    # streamlit run filename 


    # Convert to a list of tuples
   #data_for_df = list(token_freq.items()) 


    # Create a DataFrame from the list of tuples
   #df = pd.DataFrame(data_for_df, columns=['Item', 'Count'])

   #st.dataframe(df) 

