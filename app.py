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

# Device type selection
device_type = st.selectbox(
    "Device Type",
    ["Camera", "Lights", "Security System", "Smart Speaker", "Thermostat"]
)

# Other inputs
user_preferences = st.slider("User Preferences", min_value=0, max_value=1, value=1, help="0 = Low, 1 = High")
energy_consumption = st.number_input("Energy Consumption (kWh/day)", min_value=0.1, max_value=10.0, value=5.05, step=0.1)
usage_hours = st.number_input("Usage Hours Per Day", min_value=0.5, max_value=24.0, value=12.0, step=0.5)
device_age = st.number_input("Device Age (Months)", min_value=1.0, max_value=59.0, value=30.0, step=1.0)
malfunction_incidents = st.slider("Malfunction Incidents", min_value=0, max_value=4, value=2)

# One-hot encoding for device type (order matters!)
device_types = [
    'DeviceType_Camera',
    'DeviceType_Lights',
    'DeviceType_Security System',
    'DeviceType_Smart Speaker',
    'DeviceType_Thermostat'
]
device_encoding = [1 if f.split("_")[1] == device_type else 0 for f in device_types]

# Predict button
if st.button("🔍 Predict Efficiency Class"):
    input_data = np.array([
        [
            usage_hours,
            energy_consumption,
            user_preferences,
            malfunction_incidents,
            device_age,
            device_encoding[0],       # DeviceType_Camera
            device_encoding[1],       # DeviceType_Lights
            device_encoding[2],       # DeviceType_Security System
            device_encoding[3],       # DeviceType_Smart Speaker
            device_encoding[4]        # DeviceType_Thermostat
        ]
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Your device is predicted to be **Efficient (1)**.")
    else:
        st.error("⚠️ Your device is predicted to be **Inefficient (0)**.")

    st.markdown("**Note**: This prediction is based on device usage patterns and reported incidents. Consider maintenance or energy-saving strategies if the device is inefficient.")
