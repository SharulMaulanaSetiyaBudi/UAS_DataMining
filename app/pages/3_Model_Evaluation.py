import streamlit as st

st.title("Model Evaluation")

st.subheader("Hasil Evaluasi Random Forest")

st.write("""
Model Random Forest berhasil digunakan untuk melakukan prediksi customer churn.

Berdasarkan hasil pengujian:
""")

st.success("Accuracy : 79%")
st.info("Precision : 79%")
st.info("Recall : 80%")
st.info("F1-Score : 79%")

st.subheader("Kesimpulan")

st.write("""
Model memiliki performa yang cukup baik dalam memprediksi customer churn
berdasarkan data pelanggan Telco Customer Churn.

Algoritma Random Forest mampu mengklasifikasikan pelanggan yang berpotensi churn
dan pelanggan yang tetap berlangganan dengan tingkat akurasi yang cukup tinggi.
""")