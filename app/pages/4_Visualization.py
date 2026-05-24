import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Visualization Dashboard")

df = pd.read_csv(
    "../dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# METRIC
st.subheader("Customer Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Customer",
    df.shape[0]
)

col2.metric(
    "Total Churn",
    df[df["Churn"] == "Yes"].shape[0]
)

col3.metric(
    "Retention Customer",
    df[df["Churn"] == "No"].shape[0]
)

# PIE CHART
st.subheader("Distribusi Customer Churn")

churn_count = df["Churn"].value_counts()

fig1, ax1 = plt.subplots(figsize=(6,6))

ax1.pie(
    churn_count.values,
    labels=churn_count.index,
    autopct="%1.1f%%"
)

st.pyplot(fig1)

# HISTOGRAM
st.subheader("Distribusi Monthly Charges")

fig2, ax2 = plt.subplots(figsize=(8,5))

ax2.hist(
    df["MonthlyCharges"],
    bins=20
)

ax2.set_xlabel("Monthly Charges")
ax2.set_ylabel("Jumlah Customer")

st.pyplot(fig2)

# TENURE
st.subheader("Distribusi Lama Berlangganan")

fig3, ax3 = plt.subplots(figsize=(8,5))

ax3.hist(
    df["tenure"],
    bins=20
)

ax3.set_xlabel("Tenure")
ax3.set_ylabel("Jumlah Customer")

st.pyplot(fig3)

with st.expander("Penjelasan Visualisasi"):

    st.write("""
    Dashboard visualisasi digunakan untuk
    membantu analisis perilaku customer,
    distribusi churn, serta karakteristik
    pelanggan berdasarkan data Telco Customer Churn.
    """)