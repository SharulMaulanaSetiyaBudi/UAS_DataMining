import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# =========================
# TITLE
# =========================
st.title("Customer Churn Prediction")

st.write("""
Halaman ini digunakan untuk melakukan
prediksi customer churn menggunakan
algoritma Random Forest Classifier.
""")

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv(
    "dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# =========================
# PREPROCESSING
# =========================
if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

# Encoding kategori
df = pd.get_dummies(df)

# =========================
# FITUR DAN TARGET
# =========================
X = df.drop("Churn_Yes", axis=1)
y = df["Churn_Yes"]

# =========================
# SPLIT DATA
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# MODEL
# =========================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# EVALUASI MODEL
# =========================
y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

cm = confusion_matrix(
    y_test,
    y_pred
)

report = classification_report(
    y_test,
    y_pred
)

# =========================
# METRIC
# =========================
st.subheader("Model Performance")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Accuracy",
    f"{accuracy:.2%}"
)

col2.metric(
    "Training Data",
    X_train.shape[0]
)

col3.metric(
    "Testing Data",
    X_test.shape[0]
)

# =========================
# CONFUSION MATRIX
# =========================
st.subheader("Confusion Matrix")

st.write(cm)

# =========================
# CLASSIFICATION REPORT
# =========================
st.subheader("Classification Report")

st.text(report)

# =========================
# INPUT USER
# =========================
st.subheader("Input Data Customer")

tenure = st.slider(
    "Lama Berlangganan",
    1,
    72,
    12
)

monthly = st.number_input(
    "Biaya Bulanan",
    0.0,
    200.0,
    70.0
)

total = st.number_input(
    "Total Biaya",
    0.0,
    10000.0,
    1000.0
)

# =========================
# TEMPLATE INPUT
# =========================
input_data = X.iloc[[0]].copy()

input_data["tenure"] = tenure
input_data["MonthlyCharges"] = monthly
input_data["TotalCharges"] = total

# =========================
# PREDIKSI
# =========================
if st.button("Prediksi"):

    with st.spinner(
        "Sedang melakukan prediksi customer..."
    ):

        hasil = model.predict(input_data)

        if hasil[0] == 1:

            st.error(
                "Pelanggan berpotensi churn"
            )

        else:

            st.success(
                "Pelanggan diprediksi tetap berlangganan"
            )