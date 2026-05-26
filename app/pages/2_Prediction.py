import streamlit as st

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

    risk = 0

    # =========================
    # TENURE
    # =========================
    if tenure <= 6:
        risk += 40

    elif tenure <= 12:
        risk += 30

    elif tenure <= 24:
        risk += 20

    elif tenure <= 48:
        risk += 10

    else:
        risk += 2

    # =========================
    # MONTHLY CHARGES
    # =========================
    if monthly >= 120:
        risk += 30

    elif monthly >= 90:
        risk += 20

    elif monthly >= 70:
        risk += 10

    else:
        risk += 5

    # =========================
    # TOTAL CHARGES
    # =========================
    if total <= 1000:
        risk += 25

    elif total <= 3000:
        risk += 15

    elif total <= 6000:
        risk += 8

    else:
        risk += 2

    # =========================
    # SENIOR CITIZEN
    # =========================
    if senior == 1:
        risk += 10

    # =========================
    # GENDER
    # =========================
    if gender == "Female":
        risk += 3

    # =========================
    # NORMALISASI
    # =========================
    if risk > 100:
        risk = 100

    # =========================
    # HASIL
    # =========================
    st.subheader("📊 Hasil Prediksi")

    st.progress(risk)

    st.write(f"Skor Risiko Churn : {risk}%")

    # =========================
    # RISIKO TINGGI
    # =========================
    if risk >= 70:

        st.error(
            "❌ Pelanggan memiliki risiko churn TINGGI."
        )

        st.warning(
            "Pelanggan kemungkinan besar berhenti berlangganan."
        )

        st.info(
            "Disarankan memberikan promo, diskon, atau peningkatan layanan."
        )

    # =========================
    # RISIKO SEDANG
    # =========================
    elif risk >= 40:

        st.warning(
            "⚠️ Pelanggan memiliki risiko churn SEDANG."
        )

        st.info(
            "Perusahaan perlu menjaga kualitas layanan pelanggan."
        )

    # =========================
    # RISIKO RENDAH
    # =========================
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

st.subheader("📌 Keterangan Sistem")

st.write("""
Prediksi customer churn dilakukan berdasarkan:

- Lama berlangganan pelanggan
- Biaya bulanan pelanggan
- Total pembayaran pelanggan
- Status senior citizen

Semakin kecil lama berlangganan dan semakin tinggi biaya bulanan,
maka risiko churn akan semakin tinggi.
""")