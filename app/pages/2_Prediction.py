import streamlit as st
import pandas as pd
import joblib

# =========================
# LOAD MODEL
# =========================
model = joblib.load("model/model.pkl")

# =========================
# PAGE CONFIG
# =========================
st.title("🔮 Customer Churn Prediction")

st.markdown("""
Prediksi kemungkinan customer churn
menggunakan Machine Learning
Random Forest Classifier.
""")

st.markdown("---")

# =========================
# INPUT SECTION
# =========================
col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "👤 Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "🧓 Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "❤️ Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "👨‍👩‍👧 Dependents",
        ["No", "Yes"]
    )

    tenure = st.slider(
        "📅 Tenure (Months)",
        0,
        72,
        12
    )

with col2:

    phone = st.selectbox(
        "📞 Phone Service",
        ["No", "Yes"]
    )

    internet = st.selectbox(
        "🌐 Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.selectbox(
        "📝 Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    monthly = st.slider(
        "💰 Monthly Charges",
        0,
        200,
        70
    )

    total = st.slider(
        "💵 Total Charges",
        0,
        10000,
        1000
    )

# =========================
# ENCODING
# =========================
gender = 1 if gender == "Male" else 0
senior = 1 if senior == "Yes" else 0
partner = 1 if partner == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0
phone = 1 if phone == "Yes" else 0

internet_map = {
    "DSL": 0,
    "Fiber optic": 1,
    "No": 2
}

contract_map = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}

internet = internet_map[internet]
contract = contract_map[contract]

# =========================
# INPUT DATAFRAME
# =========================
input_data = pd.DataFrame([{
    "gender": gender,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone,
    "InternetService": internet,
    "Contract": contract,
    "MonthlyCharges": monthly,
    "TotalCharges": total
}])

# =========================
# PREDICTION BUTTON
# =========================
st.markdown("---")

if st.button("🚀 Predict Churn"):

    try:

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(
            input_data
        )[0]

        churn_prob = round(
            probability[1] * 100,
            2
        )

        no_churn_prob = round(
            probability[0] * 100,
            2
        )

        st.markdown("## 📊 Prediction Result")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "✅ No Churn Probability",
                f"{no_churn_prob}%"
            )

        with col2:

            st.metric(
                "⚠️ Churn Probability",
                f"{churn_prob}%"
            )

        st.markdown("---")

        if prediction == 1:

            st.error("""
⚠️ Customer diprediksi
berpotensi melakukan churn.
""")

        else:

            st.success("""
✅ Customer diprediksi
tidak melakukan churn.
""")

        # Progress bar
        st.progress(
            int(churn_prob)
        )

    except Exception as e:

        st.error("""
❌ Terjadi error pada model prediction.
""")

        st.code(str(e))