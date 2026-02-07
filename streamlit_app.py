import streamlit as st
import pandas as pd
import joblib

# 1. Page Config
st.set_page_config(page_title="CARDIO-GUARD", page_icon="🫀")

# 2. Load the model
@st.cache_resource
def load_model():
    return joblib.load("backend/model.joblib")

model = load_model()

# 3. UI Header
st.title("🫀 CARDIO-GUARD")
st.subheader("Early Cardiovascular Disease Risk Prediction")

# 4. Input Form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=50)
        sex = st.selectbox("Sex (1=M, 0=F)", [1, 0])
        cp = st.slider("Chest Pain Type (0-3)", 0, 3, 1)
        trestbps = st.number_input("Resting BP", 80, 200, 120)
        chol = st.number_input("Cholesterol", 100, 600, 200)
        fbs = st.selectbox("Fasting Blood Sugar > 120 (1=True, 0=False)", [0, 1])
    
    with col2:
        restecg = st.slider("Resting ECG (0-2)", 0, 2, 0)
        thalach = st.number_input("Max Heart Rate", 60, 220, 150)
        exang = st.selectbox("Exercise Angina (1=Yes, 0=No)", [0, 1])
        oldpeak = st.number_input("ST Depression", 0.0, 6.0, 1.0)
        slope = st.slider("ST Slope (0-2)", 0, 2, 1)
        ca = st.slider("Major Vessels (0-4)", 0, 4, 0)
        thal = st.slider("Thalassemia (0-3)", 0, 3, 2)

    submit = st.form_submit_button("Predict Risk")

# 5. Prediction Logic
if submit:
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]], 
                              columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])
    
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error(f"High Risk Detected! (Confidence: {max(prob[0])*100:.2f}%)")
    else:
        st.success(f"Low Risk Detected. (Confidence: {max(prob[0])*100:.2f}%)")
