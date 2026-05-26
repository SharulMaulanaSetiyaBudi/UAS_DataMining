import streamlit as st
import pandas as pd

st.title("📊 Dataset Overview")

df = pd.read_csv(
    "dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

st.markdown("## 🔍 Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Rows",
        df.shape[0]
    )

with col2:
    st.metric(
        "Columns",
        df.shape[1]
    )

with col3:
    st.metric(
        "Missing Values",
        df.isnull().sum().sum()
    )

st.markdown("---")

st.markdown("## 📈 Churn Distribution")

st.bar_chart(
    df["Churn"].value_counts()
)