import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("🐟 Tanzania Fish Price Prediction App")
st.write("Enter fish details below:")

# User Inputs
weight = st.number_input("Weight (grams)")
length = st.number_input("Length (cm)")
width = st.number_input("Width (cm)")

species = st.selectbox("Species", ["Dagaa", "Nile Perch", "Sardine", "Tilapia"])
market = st.selectbox("Market", ["Dar es Salaam", "Dodoma", "Mbeya", "Mwanza"])

# Create input dictionary with same columns as training
input_data = {
    "Weight_grams": weight,
    "Length_cm": length,
    "Width_cm": width,
    "Species_Dagaa": 0,
    "Species_Nile Perch": 0,
    "Species_Sardine": 0,
    "Species_Tilapia": 0,
    "Market_Dar es Salaam": 0,
    "Market_Dodoma": 0,
    "Market_Mbeya": 0,
    "Market_Mwanza": 0
}

# Encode species and market
input_data[f"Species_{species}"] = 1
input_data[f"Market_{market}"] = 1

input_df = pd.DataFrame([input_data])

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Fish Price: {prediction[0]:,.0f} TZS")
