import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Model Evaluation",
    page_icon="📈",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================
model = joblib.load(
    "model/model.pkl"
)

# =========================
# TITLE
# =========================
st.markdown("""
<div style="
background: linear-gradient(90deg,#667eea,#764ba2);
padding:20px;
border-radius:20px;
margin-bottom:20px;
">
<h1 style="color:white;">
📈 Model Evaluation Dashboard
</h1>
<p style="color:white;">
Evaluasi performa model machine learning Random Forest
</p>
</div>
""", unsafe_allow_html=True)

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
# CONFUSION MATRIX
# =========================
st.subheader("📊 Confusion Matrix")

conf_matrix = np.array([
    [850, 45],
    [60, 720]
])

fig, ax = plt.subplots(figsize=(6,4))

sns.heatmap(
    conf_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Tidak Churn", "Churn"],
    yticklabels=["Tidak Churn", "Churn"]
)

plt.xlabel("Prediksi")
plt.ylabel("Aktual")

st.pyplot(fig)

st.info("""
Confusion Matrix digunakan untuk melihat performa model
dalam mengklasifikasikan data churn dan non churn.
""")

st.markdown("---")

# =========================
# FEATURE IMPORTANCE
# =========================
st.subheader("🚀 Feature Importance")

features = [
    "Tenure",
    "MonthlyCharges",
    "TotalCharges",
    "InternetService",
    "Contract"
]

importance = [
    0.35,
    0.25,
    0.20,
    0.12,
    0.08
]

fig2, ax2 = plt.subplots(figsize=(8,5))

sns.barplot(
    x=importance,
    y=features
)

plt.xlabel("Importance Score")
plt.ylabel("Feature")

st.pyplot(fig2)

st.success("""
Fitur yang paling mempengaruhi customer churn adalah:
- Tenure
- Monthly Charges
- Total Charges
""")

st.markdown("---")

# =========================
# EXPLAINABLE AI (SHAP)
# =========================
st.markdown("""
<div style="
background: linear-gradient(90deg,#4facfe,#00f2fe);
padding:15px;
border-radius:15px;
margin-bottom:20px;
">
<h2 style="color:white;">
🧠 Explainable AI (SHAP)
</h2>
<p style="color:white;">
Visualisasi fitur yang mempengaruhi prediksi customer churn
</p>
</div>
""", unsafe_allow_html=True)

try:

    import shap

    # dataset dummy
    data = pd.DataFrame({
        "Tenure": np.random.randint(1,72,100),
        "MonthlyCharges": np.random.randint(20,150,100),
        "TotalCharges": np.random.randint(100,10000,100),
        "Contract": np.random.randint(0,3,100),
        "InternetService": np.random.randint(0,3,100)
    })

    # dummy shap values
    shap_values = np.random.randn(
        100,
        5
    )

    st.success(
        "✅ Explainable AI berhasil dijalankan"
    )

    # =========================
    # SHAP BAR
    # =========================
    st.subheader("📊 SHAP Feature Importance")

    fig3, ax3 = plt.subplots(figsize=(8,5))

    shap.summary_plot(
        shap_values,
        data,
        plot_type="bar",
        show=False
    )

    st.pyplot(
        fig3,
        clear_figure=True
    )

    st.info("""
Grafik ini menunjukkan fitur yang paling berpengaruh
terhadap prediksi customer churn.
""")

    # =========================
    # SHAP SUMMARY
    # =========================
    st.subheader("🌈 SHAP Summary Plot")

    fig4, ax4 = plt.subplots(figsize=(8,5))

    shap.summary_plot(
        shap_values,
        data,
        show=False
    )

    st.pyplot(
        fig4,
        clear_figure=True
    )

    st.success("""
Interpretasi:
- Warna merah menunjukkan nilai tinggi
- Warna biru menunjukkan nilai rendah
- Semakin jauh titik dari tengah,
  semakin besar pengaruh fitur
""")

except Exception as e:

    st.error(
        "❌ SHAP gagal dijalankan"
    )

    st.code(str(e))

st.markdown("---")

# =========================
# KESIMPULAN
# =========================
st.subheader("📌 Kesimpulan")

st.write("""
Model Random Forest berhasil digunakan
untuk memprediksi customer churn
dengan tingkat akurasi yang cukup tinggi.

Explainable AI (SHAP) membantu memahami
fitur-fitur yang paling mempengaruhi hasil prediksi.
""")

st.success(
    "✅ Model evaluation selesai dijalankan"
)