# Load CSS
with open("app/assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
import streamlit as st

# =========================
# CONFIG PAGE
# =========================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("📌 Navigation Menu")

st.sidebar.info("""
Customer Churn Prediction System
Menggunakan Machine Learning
Random Forest Classifier
""")

st.sidebar.success("UAS Data Mining")

# =========================
# MAIN PAGE
# =========================
st.title("📊 Customer Churn Prediction System")

st.image(
    "https://cdn-icons-png.flaticon.com/512/2721/2721297.png",
    width=150
)

st.write("""
Aplikasi ini digunakan untuk melakukan prediksi
customer churn menggunakan algoritma
Random Forest Classifier.
""")

# =========================
# LATAR BELAKANG
# =========================
st.subheader("Latar Belakang")

st.write("""
Customer churn merupakan kondisi ketika pelanggan
berhenti menggunakan layanan perusahaan.

Dengan memanfaatkan teknik Data Mining,
perusahaan dapat memprediksi pelanggan
yang berpotensi churn sehingga dapat
melakukan strategi pencegahan lebih awal.
""")

# =========================
# TUJUAN
# =========================
st.subheader("Tujuan Sistem")

st.write("""
- Melakukan analisis dataset customer churn
- Menampilkan visualisasi data pelanggan
- Melakukan prediksi customer churn
- Mengevaluasi performa model machine learning
""")

# =========================
# ALGORITMA
# =========================
st.subheader("Algoritma yang Digunakan")

st.info("Random Forest Classifier")

# =========================
# TOOLS
# =========================
st.subheader("Tools dan Library")

st.write("""
- Python
- Pandas
- Scikit-Learn
- Matplotlib
- Streamlit
""")

# =========================
# ANGGOTA
# =========================
st.subheader("Anggota Kelompok")

st.write("""
1. Sharul Maulana Setiya Budi - 24051214219  
2. Rafi Athillah F - 24051214213
""")

# =========================
# STATUS
# =========================
st.success("✅ Sistem berhasil dijalankan")

st.markdown("---")

st.caption(
    "UAS Data Mining | Customer Churn Prediction System"
)