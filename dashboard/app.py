import streamlit as st
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

df = pd.read_csv("data/health_dataset.csv")
model = pickle.load(open("model/risk_model.pkl","rb"))

st.title("AI Digital Health Twin Dashboard")


left, right = st.columns([2,1])


with left:

    st.subheader("New Patient Health Entry")

    heart_rate = st.slider("Heart Rate",50,120,80)
    sleep = st.slider("Sleep Hours",3.0,10.0,7.0)
    steps = st.slider("Daily Steps",1000,15000,6000)
    bp = st.slider("Blood Pressure",90,160,120)
    bmi = st.slider("BMI",18.0,40.0,24.0)

    smoking = st.selectbox("Smoking Status",["Yes","No"])
    exercise = st.selectbox("Exercise Frequency",
                            ["None","Low","Moderate","High"])

    if st.button("Predict Health Risk"):

        input_data = pd.DataFrame({
            "age":[35],
            "gender":[1],
            "heart_rate":[heart_rate],
            "sleep_hours":[sleep],
            "daily_steps":[steps],
            "blood_pressure":[bp],
            "stress_level":[5],
            "bmi":[bmi],
            "smoking_status":[1 if smoking=="Yes" else 0],
            "exercise_frequency":[2]
        })

        prediction = model.predict(input_data)

        risk_map = {0:"Low Risk",1:"Medium Risk",2:"High Risk"}

        st.success(f"Predicted Health Risk: {risk_map[prediction[0]]}")

        if prediction[0] == 2:
            st.warning("⚠ High health risk detected. Consider lifestyle improvement.")
        elif prediction[0] == 1:
            st.info("Moderate health risk. Monitor sleep and exercise.")
        else:
            st.success("Healthy lifestyle detected.")



with right:
    st.subheader("Patient Dataset")
    st.dataframe(df,height=350)



st.markdown("---")

col1,col2,col3 = st.columns(3)

with col1:
    st.subheader("BMI Distribution")
    fig,ax = plt.subplots()
    sns.histplot(df["bmi"],bins=20,ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Heart Rate vs Stress")
    fig2,ax2 = plt.subplots()
    sns.scatterplot(x="stress_level",y="heart_rate",data=df,ax=ax2)
    st.pyplot(fig2)

with col3:
    st.subheader("Daily Steps vs BMI")
    fig3,ax3 = plt.subplots()
    sns.scatterplot(x="daily_steps",y="bmi",data=df,ax=ax3)
    st.pyplot(fig3)