import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Konfigurasi Halaman Wide Layout
st.set_page_config(page_title="Prediksi Risiko Diabetes", page_icon="🩺", layout="wide")

# Load model dan artefak
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("diabetes_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("diabetes_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

with open("diabetes_kolom_kategorikal.pkl", "rb") as f:
    kolom_kategorikal = pickle.load(f)

# Header Utama
st.title("🩺 Aplikasi Prediksi Risiko Diabetes")
st.write("Masukkan data medis dan gaya hidup pasien di bawah ini:")
st.markdown("---")

# Distribusi Input Seimbang di 3 Kolom (12-12-12 input per kolom)
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👤 Profil Fisik & Vital")
    age = st.number_input("Umur", min_value=1, max_value=100, value=30)
    gender = st.selectbox("Jenis Kelamin", ["Male", "Female", "Other"])
    country = st.selectbox("Negara", ["Indonesia", "Malaysia", "Japan", "United States"])
    height = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=220.0, value=165.0)
    weight = st.number_input("Berat Badan (kg)", min_value=20.0, max_value=200.0, value=65.0)

    bmi = round(weight / ((height / 100) ** 2), 1)
    st.info(f"**BMI Terhitung:** {bmi} kg/m²")

    bp_sys = st.number_input("Tekanan Darah Sistolik", min_value=70, max_value=220, value=120)
    bp_dia = st.number_input("Tekanan Darah Diastolik", min_value=40, max_value=140, value=80)
    heart_rate = st.number_input("Detak Jantung (bpm)", min_value=40, max_value=160, value=72)
    work_type = st.selectbox("Tipe Pekerjaan", ["Private", "Government", "Student", "Retired"])
    residence = st.selectbox("Tipe Tempat Tinggal", ["Urban", "Rural"])

with col2:
    st.subheader("🩸 Hasil Laboratorium & Darah")
    blood_glucose = st.number_input("Glukosa Darah (mg/dL)", min_value=50.0, max_value=300.0, value=110.0)
    hba1c = st.number_input("HbA1c (%)", min_value=3.0, max_value=15.0, value=5.5)
    fasting_sugar = st.number_input("Gula Darah Puasa (mg/dL)", min_value=50.0, max_value=300.0, value=95.0)
    insulin = st.number_input("Kadar Insulin", min_value=5.0, max_value=300.0, value=80.0)
    cholesterol = st.number_input("Total Kolesterol", min_value=100, max_value=400, value=190)
    hdl = st.number_input("HDL", min_value=20, max_value=100, value=50)
    ldl = st.number_input("LDL", min_value=40, max_value=300, value=110)
    triglycerides = st.number_input("Trigliserida", min_value=50, max_value=500, value=140)
    sugar_intake = st.selectbox("Konsumsi Gula", ["Low", "Moderate", "High"])
    medication = st.selectbox("Kepatuhan Obat", ["Good", "Poor", "Unknown"])

with col3:
    st.subheader("🏃 Gaya Hidup & Riwayat Medis")
    act_level = st.selectbox("Tingkat Aktivitas Fisik", ["Low", "Moderate", "High"])
    exercise_hours = st.number_input("Olahraga (Jam/Minggu)", min_value=0.0, max_value=40.0, value=3.0)
    walking_mins = st.number_input("Jalan Kaki (Menit/Hari)", min_value=0, max_value=300, value=30)
    sleep_hours = st.number_input("Jam Tidur / Hari", min_value=2.0, max_value=14.0, value=7.0)
    water_intake = st.number_input("Konsumsi Air (Liter/Hari)", min_value=0.5, max_value=8.0, value=2.0)
    diet = st.selectbox("Kualitas Diet", ["Healthy", "Poor"])
    stress = st.selectbox("Tingkat Stres", ["Low", "Moderate", "High"])
    smoking = st.selectbox("Status Merokok", ["Never", "Former", "Current"])
    alcohol = st.selectbox("Konsumsi Alkohol", ["Never", "Occasionally", "Daily"])
    family_history = st.selectbox("Riwayat Diabetes Keluarga", ["No", "Yes"])
    hypertension = st.selectbox("Hipertensi", ["No", "Yes"])
    heart_disease = st.selectbox("Penyakit Jantung", ["No", "Yes"])
    fatty_liver = st.selectbox("Fatty Liver", ["No", "Yes"])
    pcos = st.selectbox("PCOS", ["No", "Yes"])

st.markdown("---")

# Tombol Prediksi
if st.button("🚀 Jalankan Prediksi Risiko Diabetes", use_container_width=True, type="primary"):
    input_data = {
        "Age": age, "Height_cm": height, "Weight_kg": weight, "BMI": bmi,
        "Blood_Glucose": blood_glucose, "HbA1c": hba1c, "Fasting_Blood_Sugar": fasting_sugar,
        "Insulin_Level": insulin, "Blood_Pressure_Systolic": bp_sys, "Blood_Pressure_Diastolic": bp_dia,
        "Total_Cholesterol": cholesterol, "HDL": hdl, "LDL": ldl, "Triglycerides": triglycerides,
        "Heart_Rate": heart_rate, "Exercise_Hours_Per_Week": exercise_hours,
        "Daily_Walking_Minutes": walking_mins, "Sleep_Hours": sleep_hours, "Daily_Water_Intake_L": water_intake,
        "Gender": gender, "Country": country, "Physical_Activity_Level": act_level,
        "Diet_Quality": diet, "Sugar_Intake_Level": sugar_intake, "Stress_Level": stress,
        "Smoking_Status": smoking, "Alcohol_Consumption": alcohol, "Family_History_Diabetes": family_history,
        "Hypertension": hypertension, "Heart_Disease": heart_disease, "Fatty_Liver": fatty_liver,
        "PCOS": pcos, "Medication_Adherence": medication, "Work_Type": work_type, "Residence_Type": residence
    }

    df_input = pd.DataFrame([input_data])
    df_encoded = pd.get_dummies(df_input, columns=kolom_kategorikal)
    df_encoded = df_encoded.reindex(columns=model_columns, fill_value=0)
    df_scaled = scaler.transform(df_encoded)
    
    prediction = model.predict(df_scaled)[0]
    probability = model.predict_proba(df_scaled)[0][1] * 100

    st.subheader("🎯 Hasil Prediksi Analisis Risiko:")
    col_res1, col_res2 = st.columns([1, 2])
    
    with col_res1:
        if prediction == 1:
            st.error(f"⚠️ Risk Status: **RISIKO TINGGI DIABETES**")
        else:
            st.success(f"✅ Risk Status: **RISIKO RENDAH DIABETES**")
        st.metric("Skor Probabilitas", f"{probability:.1f}%")
        st.progress(min(int(probability), 100))
