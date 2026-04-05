import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from streamlit_drawable_canvas import st_canvas

# Load model
BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(BASE_DIR, "model.h5")
model = tf.keras.models.load_model(model_path)

st.set_page_config(page_title="Digit Recognizer", layout="centered")

st.title("✍️ Smart Digit Recognizer (CNN)")
st.write("Draw or upload a digit (0–9)")

# Sidebar
st.sidebar.header("Options")
mode = st.sidebar.radio("Choose Input Method:", ["Draw Digit", "Upload Image"])

# ================= DRAW CANVAS =================
if mode == "Draw Digit":
    st.subheader("🎨 Draw Digit Below")

    canvas = st_canvas(
        fill_color="black",
        stroke_width=12,
        stroke_color="white",
        background_color="black",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas",
    )

    if st.button("Predict"):
        if canvas.image_data is not None:
            img = canvas.image_data.astype("uint8")

            # Convert to grayscale
            img = np.mean(img, axis=2)

            # Resize
            img = Image.fromarray(img).resize((28, 28))

            # Normalize
            img = np.array(img) / 255.0
            img = img.reshape(1, 28, 28, 1)

            prediction = model.predict(img)
            digit = np.argmax(prediction)
            confidence = np.max(prediction)

            st.success(f"Prediction: {digit}")
            st.info(f"Confidence: {confidence:.2f}")

            # Probability Chart
            fig, ax = plt.subplots()
            ax.bar(range(10), prediction[0])
            ax.set_title("Prediction Probabilities")
            ax.set_xlabel("Digit")
            ax.set_ylabel("Confidence")
            st.pyplot(fig)

# ================= UPLOAD IMAGE =================
else:
    uploaded_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=150)

        # Preprocess
        image = image.convert("L")
        image = image.resize((28, 28))
        image = ImageOps.invert(image)

        img = np.array(image) / 255.0
        img = img.reshape(1, 28, 28, 1)

        prediction = model.predict(img)
        digit = np.argmax(prediction)
        confidence = np.max(prediction)

        st.success(f"Prediction: {digit}")
        st.info(f"Confidence: {confidence:.2f}")

        # Probability Chart
        fig, ax = plt.subplots()
        ax.bar(range(10), prediction[0])
        ax.set_title("Prediction Probabilities")
        ax.set_xlabel("Digit")
        ax.set_ylabel("Confidence")
        st.pyplot(fig)
