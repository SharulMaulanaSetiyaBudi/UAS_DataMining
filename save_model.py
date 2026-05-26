import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv(
    "dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# Hapus customerID
df = df.drop(
    columns=["customerID"]
)

# Bersihkan TotalCharges
df["TotalCharges"] = (
    df["TotalCharges"]
    .replace(" ", "0")
)

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"]
)

# Encoding otomatis SEMUA string
df = pd.get_dummies(
    df,
    drop_first=True
)

# Pisahkan fitur dan target
X = df.drop(
    columns=["Churn_Yes"]
)

y = df["Churn_Yes"]

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Training
model.fit(X, y)

# Save model
joblib.dump(
    model,
    "model/model.pkl"
)

print("MODEL BERHASIL DISIMPAN")