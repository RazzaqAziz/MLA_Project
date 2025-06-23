import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('model.pkl')

# Set page configuration
st.set_page_config(
    page_title="Smart Home Efficiency Predictor",
    layout="centered",
    initial_sidebar_state="auto"
)

st.markdown("""
    <style>
    /* Style Predict button */
    .stButton > button {
        background-color: #1f77b4;  /* blue */
        color: white !important;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
    }

    /* On hover: darker blue, keep white text */
    .stButton > button:hover {
        background-color: #155a8a;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title and instructions
st.title("Smart Home Efficiency Predictor")
st.markdown(
    "This tool predicts whether your smart home device is **efficient (1)** or **inefficient (0)** "
    "based on your usage pattern and reported incidents."
)

st.markdown("---")

# Input layout
st.subheader("Device Usage Input")
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

st.subheader("Categorical Attributes")
col4, col5 = st.columns(2)

with col4:
    user_preferences = st.radio(
        "User Preferences",
        options=[0, 1],
        index=1,
        help="0 = Low, 1 = High",
        horizontal=True
    )

with col5:
    malfunction_incidents = st.radio(
        "Malfunction Incidents",
        options=[0, 1, 2, 3, 4],
        index=2,
        horizontal=True
    )

st.markdown("---")

# Predict button
if st.button("Predict Efficiency Class"):
    input_data = np.array([[
        user_preferences,
        energy_consumption,
        usage_hours,
        device_age,
        malfunction_incidents
    ]])

    prediction = model.predict(input_data)[0]
    confidence = model.predict_proba(input_data)[0][prediction] * 100

    if prediction == 1:
        st.success("Your smart device is predicted to be **Efficient**.")
    else:
        st.error("Your smart device is predicted to be **Inefficient**.")
        
     # Custom info box in light gray
    st.markdown(f"""
        <div style='
            background-color: #f2f2f2;
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #808080;
            font-size: 16px;
        '>
            <strong>Confidence Level:</strong> {confidence:.2f}%<br>
            This prediction is based on your device's reported characteristics and usage behavior.
        </div>
    """, unsafe_allow_html=True)
