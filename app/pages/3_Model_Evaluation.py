# =========================
# EXPLAINABLE AI (SHAP)
# =========================
st.markdown("---")

st.markdown("""
<div style="
background: linear-gradient(90deg,#4facfe,#00f2fe);
padding:15px;
border-radius:15px;
margin-bottom:20px;
">
<h2 style="color:white;">
🧠 Explainable AI (SHAP)
</h2>
<p style="color:white;">
Visualisasi fitur yang paling mempengaruhi prediksi customer churn
</p>
</div>
""", unsafe_allow_html=True)

try:

    import shap
    import matplotlib.pyplot as plt
    import numpy as np

    # =========================
    # LOAD DATASET
    # =========================
    df = pd.read_csv(
        "dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    )

    # preprocessing
    df.drop(
        "customerID",
        axis=1,
        inplace=True
    )

    for col in df.columns:

        if df[col].dtype == "object":

            df[col], _ = pd.factorize(
                df[col]
            )

    X = df.drop(
        "Churn",
        axis=1
    )

    # =========================
    # SHAP EXPLAINER
    # =========================
    explainer = shap.TreeExplainer(model)

    sample_data = X.sample(
        200,
        random_state=42
    )

    shap_values = explainer.shap_values(
        sample_data
    )

    st.success(
        "✅ Explainable AI berhasil dijalankan"
    )

    # =========================
    # FEATURE IMPORTANCE
    # =========================
    st.markdown("## 📊 Feature Importance")

    st.info("""
Semakin besar nilai SHAP,
semakin besar pengaruh fitur terhadap prediksi churn pelanggan.
""")

    fig1, ax1 = plt.subplots(
        figsize=(10,6)
    )

    shap.summary_plot(
        shap_values,
        sample_data,
        plot_type="bar",
        show=False
    )

    st.pyplot(
        fig1,
        clear_figure=True
    )

    # =========================
    # SUMMARY PLOT
    # =========================
    st.markdown("## 🌈 SHAP Summary Plot")

    st.info("""
Warna merah menunjukkan nilai tinggi,
warna biru menunjukkan nilai rendah.
""")

    fig2, ax2 = plt.subplots(
        figsize=(10,6)
    )

    shap.summary_plot(
        shap_values,
        sample_data,
        show=False
    )

    st.pyplot(
        fig2,
        clear_figure=True
    )

    # =========================
    # TOP FITUR
    # =========================
    st.markdown("## 🚀 Insight Model")

    importance = np.abs(
        shap_values
    ).mean(axis=0)

    feature_importance = pd.DataFrame({
        "Fitur": sample_data.columns,
        "Importance": importance
    })

    feature_importance = feature_importance.sort_values(
        by="Importance",
        ascending=False
    )

    top3 = feature_importance.head(3)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🔥 Fitur 1",
            top3.iloc[0]["Fitur"]
        )

    with col2:
        st.metric(
            "⚡ Fitur 2",
            top3.iloc[1]["Fitur"]
        )

    with col3:
        st.metric(
            "📈 Fitur 3",
            top3.iloc[2]["Fitur"]
        )

    st.markdown("---")

    st.success("""
Model Random Forest berhasil dianalisis menggunakan Explainable AI (SHAP).
Visualisasi ini membantu memahami faktor utama penyebab customer churn.
""")

except Exception as e:

    st.error(
        "❌ SHAP gagal dijalankan"
    )

    st.code(str(e))