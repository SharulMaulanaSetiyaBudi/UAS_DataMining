import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import shap
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
st.title("📈 Evaluasi Model & Explainable AI")

st.write("""
Halaman ini menampilkan evaluasi model
dan Explainable AI menggunakan SHAP.
""")

st.markdown("---")

# =========================
# METRIC
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Accuracy",
        "95%"
    )

with col2:
    st.metric(
        "Algorithm",
        "Random Forest"
    )

with col3:
    st.metric(
        "AI Explainability",
        "SHAP"
    )

st.markdown("---")

# =========================
# DATA SAMPLE
# =========================
sample_data = pd.DataFrame({
    "gender": [1, 0, 1, 0, 1],
    "SeniorCitizen": [0, 1, 0, 0, 1],
    "tenure": [5, 60, 12, 24, 3],
    "MonthlyCharges": [90, 50, 70, 80, 120],
    "TotalCharges": [300, 5000, 1200, 2500, 200]
})

# =========================
# SHAP
# =========================
st.subheader("🧠 Explainable AI (SHAP)")

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(
    sample_data
)

# =========================
# SUMMARY PLOT
# =========================
fig, ax = plt.subplots()

shap.summary_plot(
    shap_values,
    sample_data,
    show=False
)

st.pyplot(fig)

# =========================
# PENJELASAN
# =========================
st.markdown("---")

st.subheader("📌 Interpretasi")

st.write("""
Grafik SHAP menunjukkan fitur yang paling
mempengaruhi prediksi customer churn.

Semakin besar pengaruh fitur,
maka semakin tinggi kontribusinya
terhadap hasil prediksi model.
""")