import streamlit as st
import pickle
import numpy as np

# Load model
with open("fraud_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("💳 Credit Card Fraud Detection")

st.header("Project Overview")

st.write("""
This project uses Machine Learning to detect fraudulent credit card transactions.
The final model selected was Random Forest Classifier.
""")

# Metrics
st.header("Model Performance")

st.write("Accuracy: 99.954%")
st.write("Precision: 89.130%")
st.write("Recall: 83.673%")
st.write("F1 Score: 86.316%")

# Graphs
st.header("Model Comparison")
st.image("model_comparison.png")

st.header("SHAP Explainability")
st.image("shap_summary (1).png")

# Prediction Section
st.header("Fraud Prediction")

st.write("Enter values for the 30 features:")

features = []
feature_names = [
    "Time",
    "V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
    "V11","V12","V13","V14","V15","V16","V17","V18","V19","V20",
    "V21","V22","V23","V24","V25","V26","V27","V28",
    "Amount"
]

features = []

for feature in feature_names:
    value = st.number_input(feature, value=0.0)
    features.append(value)

if st.button("Predict Transaction"):

    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")