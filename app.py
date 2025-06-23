import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('model.pkl')

st.set_page_config(page_title="Smart Home Efficiency Predictor", layout="centered")
st.title("🏠 Smart Home Efficiency Predictor")

st.markdown(
    "This tool predicts whether your smart home device is **efficient (1)** or **inefficient (0)** "
    "based on usage and device information. Fill in the details below to get started:"
)

# Layout: Side-by-side for numerical inputs
col1, col2, col3 = st.columns(3)

with col1:
    energy_consumption = st.number_input(
        "Energy Consumption (kWh/day)",
        min_value=0.1,
        max_value=10.0,
        value=5.05,
        step=0.1
    )

with col2:
    usage_hours = st.number_input(
        "Usage Hours Per Day",
        min_value=0.5,
        max_value=24.0,
        value=12.0,
        step=0.5
    )

with col3:
    device_age = st.number_input(
        "Device Age (Months)",
        min_value=1.0,
        max_value=59.0,
        value=30.0,
        step=1.0
    )

# Radio buttons for categorical/binary values
user_preferences = st.radio(
    "User Preferences",
    options=[0, 1],
    index=1,
    help="0 = Low, 1 = High",
    horizontal=True
)

malfunction_incidents = st.radio(
    "Malfunction Incidents",
    options=[0, 1, 2, 3, 4],
    index=2,
    horizontal=True
)

# Predict button
if st.button("🔍 Predict Efficiency Class"):
    input_data = np.array([[
        user_preferences,
        energy_consumption,
        usage_hours,
        device_age,
        malfunction_incidents
    ]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Your device is predicted to be **Efficient (1)**.")
    else:
        st.error("⚠️ Your device is predicted to be **Inefficient (0)**.")

    st.markdown("**Note**: This prediction is based on device usage patterns and reported incidents.")
