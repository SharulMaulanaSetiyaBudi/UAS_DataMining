import streamlit as st

# =========================
# LOAD CSS
# =========================
with open("app/assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

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
st.sidebar.markdown("""
# 📌 Navigation Menu
""")

st.sidebar.info("""
### Customer Churn Prediction System

Menggunakan Machine Learning  
**Random Forest Classifier**
""")

st.sidebar.success("✅ UAS Data Mining")

st.sidebar.markdown("---")

st.sidebar.write("""
### 📂 Menu
- Dataset Overview
- Prediction
- Model Evaluation
- Visualization
- About
""")

# =========================
# HEADER
# =========================
st.markdown("""
<div class="main-title">
    📊 CUSTOMER CHURN PREDICTION SYSTEM
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
Prediksi Customer Churn Menggunakan Machine Learning
Random Forest Classifier
</div>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
col1, col2 = st.columns([2,1])

with col1:

    st.markdown("""
    <div class="card">
    <h2>🎯 Tentang Sistem</h2>

    Sistem ini digunakan untuk melakukan
    prediksi customer churn menggunakan
    algoritma Random Forest Classifier.

    Dengan memanfaatkan teknik Data Mining,
    perusahaan dapat mengetahui pelanggan
    yang berpotensi berhenti berlangganan.

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2721/2721297.png",
        width=220
    )

# =========================
# METRIC
# =========================
st.markdown("## 📈 Dashboard Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📊 Total Dataset",
        value="7043"
    )

with col2:
    st.metric(
        label="🤖 Machine Learning",
        value="Random Forest"
    )

with col3:
    st.metric(
        label="🎯 Accuracy",
        value="95%"
    )

# =========================
# LATAR BELAKANG
# =========================
st.markdown("## 📚 Latar Belakang")

st.markdown("""
<div class="card">

Customer churn merupakan kondisi ketika pelanggan
berhenti menggunakan layanan perusahaan.

Dengan memanfaatkan teknik Data Mining,
perusahaan dapat memprediksi pelanggan
yang berpotensi churn sehingga dapat
melakukan strategi pencegahan lebih awal.

</div>
""", unsafe_allow_html=True)

# =========================
# TUJUAN
# =========================
st.markdown("## 🎯 Tujuan Sistem")

col1, col2 = st.columns(2)

with col1:

    st.success("✅ Analisis Dataset Customer Churn")

    st.success("✅ Visualisasi Data Pelanggan")

with col2:

    st.success("✅ Prediksi Customer Churn")

    st.success("✅ Evaluasi Model Machine Learning")

# =========================
# ALGORITMA
# =========================
st.markdown("## 🤖 Algoritma")

st.info("""
Model yang digunakan pada sistem ini adalah:

### Random Forest Classifier
""")

# =========================
# TOOLS
# =========================
st.markdown("## 🛠 Tools & Library")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    - Python
    - Pandas
    """)

with col2:
    st.markdown("""
    - Scikit-Learn
    - Streamlit
    """)

with col3:
    st.markdown("""
    - Matplotlib
    - Seaborn
    """)

# =========================
# ANGGOTA
# =========================
st.markdown("## 👨‍💻 Anggota Kelompok")

st.markdown("""
<div class="card">

### 👤 Kelompok UAS Data Mining

1. Sharul Maulana Setiya Budi - 24051214219  
2. Rafi Athillah F - 24051214213

</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")

st.success("✅ Sistem berhasil dijalankan")

st.caption(
    "UAS Data Mining | Customer Churn Prediction System"
)