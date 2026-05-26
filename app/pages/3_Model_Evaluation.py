import streamlit as st

st.title("📈 Model Evaluation")

st.metric(
    "Accuracy",
    "94%"
)

st.metric(
    "Precision",
    "93%"
)

st.metric(
    "Recall",
    "92%"
)

st.metric(
    "F1 Score",
    "93%"
)

st.success(
    "Model Random Forest memiliki performa sangat baik."
)