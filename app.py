import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('model.pkl')

st.title("Smart Home Efficiency Predictor")

# Input form
user_preferences = st.slider("User Preferences (1-5)", 1, 5, 3)
energy_consumption = st.number_input("Energy Consumption (kWh)", min_value=0.0, value=50.0)
usage_hours = st.number_input("Usage Hours Per Day", min_value=0.0, value=4.5)
device_age = st.number_input("Device Age (months)", min_value=0.0, value=12.0)
malfunction_incidents = st.number_input("Malfunction Incidents", min_value=0, value=1)

# Predict button
if st.button("Predict Efficiency Class"):
    input_data = np.array([[user_preferences, energy_consumption, usage_hours, device_age, malfunction_incidents]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Smart Home Efficiency Class: {prediction}")
