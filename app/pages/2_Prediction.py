import streamlit as st
import pandas as pd
import joblib

model = joblib.load(
    "model/model.pkl"
)

st.title("🤖 Customer Churn Prediction")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior = st.slider(
    "Senior Citizen",
    0,
    1
)

tenure = st.slider(
    "Tenure",
    0,
    72
)

monthly = st.slider(
    "Monthly Charges",
    0,
    200
)

total = st.slider(
    "Total Charges",
    0,
    10000
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "SeniorCitizen":[senior],
        "tenure":[tenure],
        "MonthlyCharges":[monthly],
        "TotalCharges":[total]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:

        st.error(
            "⚠️ Customer kemungkinan CHURN"
        )

    else:

        st.success(
            "✅ Customer kemungkinan TIDAK CHURN"
        )