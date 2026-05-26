import streamlit as st
import pandas as pd
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
st.title("🔮 Prediksi Customer Churn")

st.write("""
Masukkan data pelanggan untuk melakukan
prediksi customer churn.
""")

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
        0,
        72,
        12
    )

with col2:

    monthly = st.slider(
        "Biaya Bulanan",
        0,
        200,
        70
    )

    total = st.slider(
        "Total Biaya",
        0,
        10000,
        1000
    )

# =========================
# ENCODING
# =========================
gender = 1 if gender == "Male" else 0

# =========================
# FORMAT DATA
# =========================
input_data = pd.DataFrame([{
    "gender": gender,
    "SeniorCitizen": senior,
    "tenure": tenure,
    "MonthlyCharges": monthly,
    "TotalCharges": total
}])

# =========================
# TAMBAH FITUR KOSONG
# =========================
fitur_model = [
    'gender',
    'SeniorCitizen',
    'Partner',
    'Dependents',
    'tenure',
    'PhoneService',
    'MultipleLines',
    'InternetService',
    'OnlineSecurity',
    'OnlineBackup',
    'DeviceProtection',
    'TechSupport',
    'StreamingTV',
    'StreamingMovies',
    'Contract',
    'PaperlessBilling',
    'PaymentMethod',
    'MonthlyCharges',
    'TotalCharges'
]

for col in fitur_model:

    if col not in input_data.columns:

        input_data[col] = 0

input_data = input_data[fitur_model]

# =========================
# PREDICTION
# =========================
if st.button("🚀 Prediksi"):

    prediction = model.predict(
        input_data
    )[0]

    probability = model.predict_proba(
        input_data
    )[0]

    churn = round(
        probability[1] * 100,
        2
    )

    not_churn = round(
        probability[0] * 100,
        2
    )

    st.markdown("---")

    st.subheader("📊 Hasil Prediksi")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Tidak Churn",
            f"{not_churn}%"
        )

    with col2:

        st.metric(
            "Churn",
            f"{churn}%"
        )

    st.progress(
        int(churn)
    )

    if prediction == 1:

        st.error("""
⚠️ Customer diprediksi
berpotensi churn
""")

    else:

        st.success("""
✅ Customer diprediksi
tidak churn
""")