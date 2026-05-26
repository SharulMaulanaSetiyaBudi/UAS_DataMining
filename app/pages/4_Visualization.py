import streamlit as st
import pandas as pd

st.title("📊 Visualization Dashboard")

df = pd.read_csv(
    "dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

st.markdown("## Monthly Charges")

st.line_chart(
    df["MonthlyCharges"]
)

st.markdown("## Tenure")

st.area_chart(
    df["tenure"]
)

st.markdown("## Churn")

st.bar_chart(
    df["Churn"].value_counts()
)