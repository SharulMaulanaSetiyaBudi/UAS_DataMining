import streamlit as st

# =========================
# CONFIG PAGE
# =========================
st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

# =========================
# CUSTOM HEADER
# =========================
st.markdown("""
<div style="
background: linear-gradient(90deg,#667eea,#764ba2);
padding:20px;
border-radius:20px;
margin-bottom:20px;
">
<h1 style="color:white;">
ℹ️ About Project
</h1>
<p style="color:white;">
Informasi project Customer Churn Prediction System
</p>
</div>
""", unsafe_allow_html=True)

# =========================
# DESKRIPSI
# =========================
st.subheader("📌 Tentang Project")

st.write("""
Project ini dibuat untuk memprediksi customer churn
menggunakan algoritma Machine Learning Random Forest Classifier.

Sistem dapat membantu perusahaan mengetahui pelanggan
yang berpotensi berhenti berlangganan sehingga perusahaan
dapat melakukan strategi pencegahan lebih awal.
""")

st.markdown("---")

# =========================
# ALGORITMA
# =========================
st.subheader("🤖 Algoritma")

st.info("""
Random Forest Classifier
""")

st.write("""
Random Forest dipilih karena memiliki akurasi yang tinggi,
stabil terhadap data besar, dan mampu menangani
fitur numerik maupun kategorikal dengan baik.
""")

st.markdown("---")

# =========================
# EXPLAINABLE AI
# =========================
st.subheader("🧠 Explainable AI (SHAP)")

st.success("""
Project ini menggunakan SHAP
(SHapley Additive Explanations)
untuk menjelaskan fitur-fitur
yang paling mempengaruhi hasil prediksi.
""")

st.write("""
Dengan SHAP, model machine learning menjadi lebih transparan
karena pengguna dapat mengetahui alasan model
menghasilkan prediksi tertentu.
""")

st.markdown("---")

# =========================
# TOOLS
# =========================
st.subheader("🛠️ Tools dan Library")

col1, col2 = st.columns(2)

with col1:

    st.write("""
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
""")

with col2:

    st.write("""
- Scikit-Learn
- Streamlit
- Joblib
- SHAP
- Random Forest
""")

st.markdown("---")

# =========================
# DATASET
# =========================
st.subheader("🗂️ Dataset")

st.info("""
Dataset yang digunakan:
WA_Fn-UseC_-Telco-Customer-Churn.csv
""")

st.write("""
Dataset berisi informasi pelanggan telco seperti:
- Gender
- Lama berlangganan
- Internet service
- Total biaya
- Monthly charges
- Status churn pelanggan
""")

st.markdown("---")

# =========================
# FITUR SISTEM
# =========================
st.subheader("🚀 Fitur Sistem")

col1, col2 = st.columns(2)

with col1:

    st.success("✅ Dataset Overview")
    st.success("✅ Visualisasi Data")
    st.success("✅ Prediksi Customer Churn")

with col2:

    st.success("✅ Model Evaluation")
    st.success("✅ Explainable AI SHAP")
    st.success("✅ Dashboard Interaktif")

st.markdown("---")

# =========================
# ANGGOTA
# =========================
st.subheader("👨‍💻 Anggota Kelompok")

st.write("""
1. Sharul Maulana Setiya Budi - 24051214219  
2. Rafi Athillah F - 24051214213
""")

st.markdown("---")

# =========================
# STATUS
# =========================
st.success("""
✅ Project berhasil dijalankan
""")

st.info("""
UAS Data Mining
Customer Churn Prediction System
""")