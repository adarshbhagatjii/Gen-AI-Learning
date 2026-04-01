import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os

BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(BASE_DIR, "next_word_lstm.h5")

model = tf.keras.models.load_model(model_path)

with open(os.path.join(BASE_DIR, 'tokenizer.pickle'), 'rb') as file:
    tokenizer=pickle.load(file)


# Function to predict the next word
def predict_next_word(model, tokenizer, text, max_sequence_len):
    token_list=tokenizer.texts_to_sequences([text])[0]
    if len(token_list)>=max_sequence_len:
        token_list=token_list[-(max_sequence_len-1):] #Ensure the sequence length matches max_sequence
    token_list=pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted=model.predict(token_list, verbose=0)
    predicted_word_index=np.argmax(predicted, axis=1)
    for word, index in tokenizer.word_index.items():
        if index==predicted_word_index:
            return word
    return None



st.title("Next Word Prediction with LSTM")
input_text=st.text_input("Enter a sequence of words:")
if st.button("Predict"):
    if input_text:
        max_sequence_len=model.input_shape[1]
        predicted_word=predict_next_word(model, tokenizer, input_text, max_sequence_len)
        if predicted_word:
            st.write(f"Predicted next word: {predicted_word}")
        else:
            st.write("Could not predict the next word.")
    else:
        st.write("Please enter some text to predict the next word.")