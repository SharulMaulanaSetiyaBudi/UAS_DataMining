import streamlit as st

st.title("About Project")

st.subheader("Customer Churn Prediction System")

st.write("""
Project ini dibuat untuk memenuhi tugas UAS Data Mining.

Aplikasi menggunakan algoritma Random Forest
untuk memprediksi customer churn berdasarkan
dataset Telco Customer Churn.
""")

st.subheader("Fitur Sistem")

st.write("""
- Dataset Overview
- Visualization
- Customer Churn Prediction
- Model Evaluation
""")

st.subheader("Algoritma")

st.info("Random Forest Classifier")

st.subheader("Tools dan Library")

st.write("""
- Python
- Pandas
- Scikit-Learn
- Matplotlib
- Streamlit
""")

st.subheader("Dataset")

st.write("""
Dataset yang digunakan:
WA_Fn-UseC_-Telco-Customer-Churn.csv
""")

st.subheader("Anggota Kelompok")

st.write("""
1. Sharul Maulana Setiya Budi - 24051214219
2. Rafi Athilla F - 24051214213
""")

st.success("Project berhasil dijalankan")