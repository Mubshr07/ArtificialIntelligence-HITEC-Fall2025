import streamlit as st
import joblib
import numpy as np
# Load model
model = joblib.load("hydration_model.pkl")

st.title("💧 Hydration Level Prediction App")
st.write("Enter your details to predict hydration level:")

# Show how many features model expects
try:
    st.info(f"Model expects features: {model.n_features_in_}")
except:
    pass

# User inputs
age = st.number_input("Enter Age", min_value=1, max_value=100, value=25)
weight = st.number_input("Enter Weight (kg)", min_value=1.0, max_value=200.0, value=60.0)
daily_water = st.number_input("Enter Daily Water Intake (liters)", min_value=0.0, max_value=10.0, value=2.0)

activity = st.selectbox("Physical Activity Level", ["Low", "Moderate", "High"])
weather = st.selectbox("Weather", ["Cold", "Normal", "Hot"])

# Convert activity to dummy variables (as per training)
activity_low = 1 if activity == "Low" else 0
activity_moderate = 1 if activity == "Moderate" else 0

# Convert weather to dummy variables (as per training)
weather_hot = 1 if weather == "Hot" else 0
weather_normal = 1 if weather == "Normal" else 0

# Final input in EXACT order model was trained on
input_data = np.array([[
    age,
    weight,
    daily_water,
    activity_low,
    activity_moderate,
    weather_hot,
    weather_normal
]])

# Predict button
if st.button("Predict Hydration Level"):
    prediction = model.predict(input_data)

    # Rule-based correction (to make project intelligent & realistic)
    if daily_water < 1.5:
        result = "❌ Poor Hydration"
    else:
        if prediction[0] == True:
            result = "✅ Good Hydration"
        else:
            result = "❌ Poor Hydration"

    st.success(f"Predicted Hydration Level: {result}")