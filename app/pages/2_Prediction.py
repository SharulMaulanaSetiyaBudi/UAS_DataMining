import streamlit as st
import pandas as pd
import random

# =========================
# TITLE
# =========================
st.title("🔮 Prediksi Customer Churn")

st.write(
    "Masukkan data pelanggan untuk melakukan prediksi customer churn."
)

st.markdown("---")

# =========================
# INPUT
# =========================
col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Jenis Kelamin",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    tenure = st.slider(
        "Lama Berlangganan (Bulan)",
        1,
        72,
        12
    )

with col2:

    monthly = st.slider(
        "Biaya Bulanan",
        10,
        150,
        70
    )

    total = st.slider(
        "Total Biaya",
        0,
        10000,
        1000
    )

st.markdown("---")

# =========================
# PREDIKSI
# =========================
if st.button("🚀 Prediksi"):

    score = 0

    if tenure < 12:
        score += 1

    if monthly > 80:
        score += 1

    if total < 2000:
        score += 1

    if senior == 1:
        score += 1

    if gender == "Female":
        score += 1

    # =========================
    # HASIL
    # =========================
    if score >= 3:

        st.error(
            "❌ Pelanggan berpotensi churn."
        )

        st.warning(
            "Disarankan memberikan promo atau penawaran khusus."
        )

    else:

        st.success(
            "✅ Pelanggan kemungkinan tetap berlangganan."
        )

        st.info(
            "Pelanggan memiliki loyalitas yang cukup baik."
        )

# =========================
# KETERANGAN
# =========================
st.markdown("---")

st.subheader("📌 Keterangan")

st.write("""
Sistem ini melakukan simulasi prediksi customer churn
berdasarkan beberapa faktor pelanggan seperti:

- Lama berlangganan
- Biaya bulanan
- Total pembayaran
- Status senior citizen
- Jenis kelamin

Semakin tinggi skor risiko maka pelanggan
diprediksi berpotensi churn.
""")