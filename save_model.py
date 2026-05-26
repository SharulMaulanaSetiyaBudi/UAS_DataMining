import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv(
    "dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# =========================
# PILIH FITUR
# =========================
df = df[[
    "gender",
    "SeniorCitizen",
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "Churn"
]]

# =========================
# BERSIHKAN DATA
# =========================
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

# =========================
# ENCODING
# =========================
df["gender"] = df["gender"].map({
    "Male": 1,
    "Female": 0
})

df["Churn"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

# =========================
# FEATURE & TARGET
# =========================
X = df.drop(
    "Churn",
    axis=1
)

y = df["Churn"]

# =========================
# MODEL
# =========================
model = RandomForestClassifier(
    random_state=42
)

# =========================
# TRAINING
# =========================
model.fit(X, y)

# =========================
# SAVE MODEL
# =========================
joblib.dump(
    model,
    "model/model.pkl"
)

print("MODEL BERHASIL DISIMPAN")