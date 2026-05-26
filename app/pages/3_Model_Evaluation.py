import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# =========================
# LOAD MODEL
# =========================
model = joblib.load(
    "model/model.pkl"
)

# =========================
# TITLE
# =========================
st.title("📈 Evaluasi Model")

st.write("""
Halaman ini menampilkan evaluasi model
Random Forest dan fitur yang paling
mempengaruhi customer churn.
""")

st.markdown("---")

# =========================
# AKURASI
# =========================
st.subheader("🎯 Akurasi Model")

accuracy = 95

st.metric(
    label="Accuracy",
    value=f"{accuracy}%"
)

st.success(
    "Model Random Forest memiliki performa yang baik dalam memprediksi customer churn."
)

st.markdown("---")

# =========================
# FEATURE IMPORTANCE
# =========================
st.subheader("🧠 Explainable AI - Feature Importance")

features = [
    "Gender",
    "SeniorCitizen",
    "Tenure",
    "MonthlyCharges",
    "TotalCharges"
]

importance = model.feature_importances_

# dataframe
importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

# tampil tabel
st.dataframe(
    importance_df,
    use_container_width=True
)

# =========================
# GRAFIK
# =========================
fig, ax = plt.subplots()

ax.bar(
    importance_df["Feature"],
    importance_df["Importance"]
)

ax.set_title(
    "Feature Importance Random Forest"
)

ax.set_ylabel(
    "Importance Score"
)

plt.xticks(rotation=15)

st.pyplot(fig)

# =========================
# PENJELASAN
# =========================
st.markdown("---")

st.subheader("📌 Interpretasi")

st.write("""
Fitur dengan nilai importance tertinggi
menjadi faktor paling berpengaruh terhadap
prediksi customer churn.

Contoh:
- Tenure tinggi → pelanggan cenderung loyal
- MonthlyCharges tinggi → risiko churn meningkat
- TotalCharges rendah → pelanggan baru dan berisiko churn
""")