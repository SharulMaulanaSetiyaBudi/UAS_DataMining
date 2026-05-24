import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dataset Overview")

df = pd.read_csv(
    "../dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

st.subheader("Preview Dataset")

st.dataframe(df.head())

st.subheader("Informasi Dataset")

st.write(f"Jumlah Baris : {df.shape[0]}")
st.write(f"Jumlah Kolom : {df.shape[1]}")

st.subheader("Daftar Kolom")

st.write(df.columns.tolist())

# Visualisasi churn
st.subheader("Visualisasi Customer Churn")

churn_count = df["Churn"].value_counts()

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    churn_count.index,
    churn_count.values
)

ax.set_xlabel("Status Churn")
ax.set_ylabel("Jumlah Customer")
ax.set_title("Distribusi Customer Churn")

st.pyplot(fig)

# Missing values
st.subheader("Missing Values")

st.write(df.isnull().sum())