import streamlit as st
import pandas as pd
import joblib

model = joblib.load('LR_heart.pkl')
scaler = joblib.load('scaler_heart.pkl')
expected_columns = joblib.load('columns_heart.pkl')

st.title("Heart Stroke Prediction by akarsh")
st.markdown("Provide the following details")

age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ['M', 'F'])
chestPain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
bp = st.number_input("Resting Blood Pressure" , 80, 200, 120)
cholesterol = st.number_input("Cholesterol(mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
excercise_angina = st.selectbox("Exercise-Induced Angina", ['Y', 'N'])
oldPeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):
    raw_input = {
        "Age": age,
        "RestingBP": bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldPeak,
        "Sex_"+ sex: 1,
        "ChestPainType_"+chestPain: 1,
        "RestingECG_" + excercise_angina: 1,
        "ST_Slope_" + slope: 1
    }

    df = pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0


    df = df[expected_columns]
    prediction = model.predict(df)[0]
    if prediction == 1:
        st.error("High Risk of Heart Disease")
    else:
        st.success("Low Risk of Heart Disease")