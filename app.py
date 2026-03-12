import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

model = joblib.load("heart_model.pkl")
data = pd.read_csv("heart.csv")

st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

st.title("❤️ Heart Disease Risk Prediction System")

st.sidebar.header("Patient Health Details")

age = st.sidebar.slider("Age", 20, 100, 50)
sex = st.sidebar.selectbox("Sex", ["Male", "Female"])

cp = st.sidebar.selectbox(
    "Chest Pain Type",
    ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"]
)

trestbps = st.sidebar.slider("Resting Blood Pressure", 80, 200, 120)
chol = st.sidebar.slider("Cholesterol", 100, 400, 200)

fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])

restecg = st.sidebar.selectbox(
    "Resting ECG",
    ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"]
)

thalach = st.sidebar.slider("Maximum Heart Rate Achieved", 60, 220, 150)

exang = st.sidebar.selectbox("Exercise Induced Angina", ["No", "Yes"])

oldpeak = st.sidebar.slider("ST Depression", 0.0, 6.0, 1.0)

slope = st.sidebar.selectbox("Slope of ST Segment",
["Upsloping","Flat","Downsloping"])

ca = st.sidebar.selectbox("Major Vessels", [0,1,2,3])

thal = st.sidebar.selectbox(
    "Thalassemia",
    ["Unknown","Normal","Fixed Defect","Reversible Defect"]
)

sex = 1 if sex=="Male" else 0

cp_map={
"Typical Angina":0,
"Atypical Angina":1,
"Non-Anginal Pain":2,
"Asymptomatic":3
}
cp=cp_map[cp]

fbs = 1 if fbs=="Yes" else 0

restecg_map={
"Normal":0,
"ST-T Wave Abnormality":1,
"Left Ventricular Hypertrophy":2
}
restecg=restecg_map[restecg]

exang=1 if exang=="Yes" else 0

slope_map={
"Upsloping":0,
"Flat":1,
"Downsloping":2
}
slope=slope_map[slope]

thal_map={
"Unknown":0,
"Normal":1,
"Fixed Defect":2,
"Reversible Defect":3
}
thal=thal_map[thal]

input_data=pd.DataFrame({
"age":[age],
"sex":[sex],
"cp":[cp],
"trestbps":[trestbps],
"chol":[chol],
"fbs":[fbs],
"restecg":[restecg],
"thalach":[thalach],
"exang":[exang],
"oldpeak":[oldpeak],
"slope":[slope],
"ca":[ca],
"thal":[thal]
})

if st.button("Predict Heart Disease Risk"):

    prediction=model.predict(input_data)
    probability=model.predict_proba(input_data)

    risk_score=probability[0][1]

    st.subheader("Prediction Result")

    if prediction[0]==1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

    st.write("### Risk Probability")
    st.progress(float(risk_score))
    st.write(f"Risk Score: **{round(risk_score*100,2)} %**")

    fig,ax=plt.subplots()

    labels=["No Disease","Heart Disease"]
    values=probability[0]

    ax.bar(labels,values)
    ax.set_title("Prediction Probability")

    st.pyplot(fig)

st.markdown("---")
st.header("📊 Dataset Visualizations")

col1,col2=st.columns(2)

with col1:

    st.subheader("Age Distribution")

    fig,ax=plt.subplots()
    ax.hist(data["age"],bins=20)
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")

    st.pyplot(fig)

with col2:

    st.subheader("Heart Disease Distribution")

    fig,ax=plt.subplots()
    data["target"].value_counts().plot(kind="bar",ax=ax)
    ax.set_xlabel("Heart Disease")
    ax.set_ylabel("Count")

    st.pyplot(fig)

st.subheader("Cholesterol vs Age")

fig,ax=plt.subplots()

ax.scatter(data["age"],data["chol"])
ax.set_xlabel("Age")
ax.set_ylabel("Cholesterol")

st.pyplot(fig)

st.subheader("Correlation Heatmap")

fig,ax=plt.subplots()

corr=data.corr()

cax=ax.matshow(corr)
fig.colorbar(cax)

ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))

ax.set_xticklabels(corr.columns,rotation=90)
ax.set_yticklabels(corr.columns)

st.pyplot(fig)

st.markdown("---")
st.write("Machine Learning Model: Supervised Learning")
st.write("Developed using Streamlit")
st.write("Developed By: E.Harikrishna 👨🏻‍💻")