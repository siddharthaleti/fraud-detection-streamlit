

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import re

# Load model
model = joblib.load("xgboost_fraud_model.pkl")

st.title("💳 Real-Time Fraud Detection (Paste & Predict)")

st.markdown("""
**Paste a single transaction as 30 values** separated by **comma `,`** or **tab `\\t`**  
👉 Example:  
`7740\t1.02\t2.00\t-4.76\t3.82\t...0.0202\t1`
""")

raw_input = st.text_area("📋 Paste transaction data here:", height=100)

if st.button("🔍 Predict Transaction"):
    try:
        # Replace tabs or multiple spaces with commas
        cleaned = re.sub(r'[\t ]+', ',', raw_input.strip())
        values = list(map(float, cleaned.split(",")))

        assert len(values) == 30, f"Expected 30 values, got {len(values)}."

        # Prepare DataFrame
        feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
        input_df = pd.DataFrame([dict(zip(feature_names, values))])

        # Prediction
        prob = model.predict_proba(input_df)[0][1]
        label = "Fraud" if prob > 0.5 else "Not Fraud"

        st.success(f"🧾 Prediction: **{label}**")
        st.write(f"📈 Probability of Fraud: **{prob:.4f}**")
        st.progress(int(prob * 100))

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
