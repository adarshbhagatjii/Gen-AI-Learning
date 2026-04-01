import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle
import os
# Load the trained model


BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(BASE_DIR, "regression_model.h5")

model = tf.keras.models.load_model(model_path)


# Load the encoders and scaler
with open(os.path.join(BASE_DIR, "label_encoder_gender.pkl"), 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open(os.path.join(BASE_DIR, "onehot_encoder_geo.pkl"), 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open(os.path.join(BASE_DIR, "scaler.pkl"), 'rb') as file:
    scaler = pickle.load(file)

# Streamlit app
st.title('💰 Estimated Salary Prediction')

# User input
geography = st.selectbox('🌍 Geography', onehot_encoder_geo.categories_[0])
gender = st.selectbox('🧍 Gender', label_encoder_gender.classes_)
age = st.slider('🎂 Age', 18, 92)
balance = st.number_input('💵 Balance')
credit_score = st.number_input('💳 Credit Score')
exited = st.selectbox('🚪 Exited', [0, 1])
tenure = st.slider('📆 Tenure', 0, 10)
num_of_products = st.slider('📦 Number of Products', 1, 4)
has_cr_card = st.selectbox('💳 Has Credit Card', [0, 1])
is_active_member = st.selectbox('✅ Is Active Member', [0, 1])

# Prepare the input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'Exited': [exited]
})

# One -hot encode "Geography"

geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()

geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))



# Combine one-hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# Scale the input data
input_scaled = scaler.transform(input_data)

# Make prediction
prediction = model.predict(input_scaled)
predicted_salary = prediction[0][0]

# Display result

st.write(f' Predicted Estimated Salary :$ {predicted_salary:,.2f}')

