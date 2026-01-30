import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# ===============================
# Load Model & Preprocessors
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

rf_model = joblib.load(os.path.join(BASE_DIR, "dns_rf_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "dns_scaler.pkl"))
label_encoder = joblib.load(os.path.join(BASE_DIR, "dns_label_encoder.pkl"))

# ===============================
# FEATURE NAMES (from your training X_reduced.columns)
# ===============================
# Replace this list with the actual top 20 features printed from your training script
feature_names = [
    "Flow Bytes/s",
    "Flow Packets/s",
    "Flow IAT Max",
    "Flow IAT Mean",
    "Flow IAT Std",
    "Fwd Packet Length Max",
    "Fwd Packet Length Min",
    "Fwd Packet Length Mean",
    "Bwd Packet Length Mean",
    "Active Mean",
    "Idle Mean",
    "Avg Packet Size",
    "Avg Fwd Segment Size",
    "Bwd Header Length",
    "Bwd IAT Max",
    "Bwd IAT Mean",
    "Packet Length Std",
    "Packet Length Mean",
    "Subflow Fwd Bytes",
    "Subflow Bwd Bytes"
]

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="DNS Attack Detection System",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ DNS Attack Detection System")
st.markdown("Artificial Intelligence – Model Deployment")
st.markdown("---")

# ===============================
# Input UI
# ===============================
st.subheader("📥 Enter DNS Feature Values")

user_input = {}

for feature in feature_names:
    user_input[feature] = st.number_input(
        label=feature,
        value=0.0,
        format="%.5f"
    )

input_df = pd.DataFrame([user_input])

# ===============================
# Prediction
# ===============================
if st.button("🔍 Predict Attack"):
    try:
        # Convert to NumPy array to avoid feature name mismatch
        scaled_input = scaler.transform(input_df.values)
        pred = rf_model.predict(scaled_input)
        prob = rf_model.predict_proba(scaled_input)

        label = label_encoder.inverse_transform(pred)[0]
        confidence = np.max(prob) * 100

        st.success(f"### ✅ Prediction: {label}")
        st.info(f"Confidence: {confidence:.2f}%")

    except Exception as e:
        st.error(f"Prediction Error: {e}")

st.markdown("---")
st.markdown("🎓 AI Project – DNS Attack Detection")
