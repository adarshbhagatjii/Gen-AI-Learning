import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(page_title="Next Word Predictor", page_icon="🧠")
st.title("🧠 Bi-Directional LSTM Next Word Predictor")

# ------------------------------------------------
# TRAINING TEXT INPUT
# ------------------------------------------------
training_text = st.text_area(
    "Enter training text (one sentence per line)",
    height=200,
    placeholder="machine learning is powerful\ndeep learning is part of ai"
)

epochs = st.slider("Training Epochs", 10, 100, 40)

# ------------------------------------------------
# TRAIN MODEL
# ------------------------------------------------
@st.cache_resource
def train_model(corpus, epochs):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([corpus])

    total_words = len(tokenizer.word_index) + 1

    input_sequences = []
    for line in corpus.split("\n"):
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            input_sequences.append(token_list[:i + 1])

    max_seq_len = max(len(seq) for seq in input_sequences)
    input_sequences = pad_sequences(input_sequences, maxlen=max_seq_len, padding="pre")

    X = input_sequences[:, :-1]
    y = input_sequences[:, -1]

    model = Sequential([
        Embedding(total_words, 100, input_length=max_seq_len - 1),
        Bidirectional(LSTM(150)),
        Dense(total_words, activation="softmax")
    ])

    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer="adam",
        metrics=["accuracy"]
    )

    model.fit(X, y, epochs=epochs, verbose=0)

    return model, tokenizer, max_seq_len

# ------------------------------------------------
# TRAIN BUTTON
# ------------------------------------------------
if st.button("Train Model"):
    if training_text.strip() == "":
        st.warning("Please enter training text")
    else:
        with st.spinner("Training model..."):
            model, tokenizer, max_seq_len = train_model(training_text.lower(), epochs)
            st.session_state.model = model
            st.session_state.tokenizer = tokenizer
            st.session_state.max_seq_len = max_seq_len
        st.success("Model trained successfully!")

# ------------------------------------------------
# NEXT WORD PREDICTION
# ------------------------------------------------
if "model" in st.session_state:
    st.subheader("🔮 Predict Next Words")

    seed_text = st.text_input("Enter seed text")
    next_words = st.slider("Number of words to predict", 1, 10, 3)

    def predict_next_word(seed_text, next_words):
        for _ in range(next_words):
            token_list = st.session_state.tokenizer.texts_to_sequences(
                [seed_text.lower()]
            )[0]

            token_list = pad_sequences(
                [token_list],
                maxlen=st.session_state.max_seq_len - 1,
                padding="pre"
            )

            predicted_index = np.argmax(
                st.session_state.model.predict(token_list, verbose=0),
                axis=-1
            )[0]

            predicted_word = st.session_state.tokenizer.index_word.get(
                predicted_index, ""
            )

            seed_text += " " + predicted_word

        return seed_text

    if st.button("Predict"):
        if seed_text.strip() == "":
            st.warning("Please enter seed text")
        else:
            result = predict_next_word(seed_text, next_words)
            st.success(f"👉 Prediction:\n\n**{result}**")
