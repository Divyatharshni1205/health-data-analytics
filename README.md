This project is a Health Data Analytics Prototype that analyzes simulated patient health data and predicts potential health risk levels using machine learning. The system demonstrates how a simplified Digital Health Twin analytics system could monitor lifestyle indicators and provide insights for preventive healthcare.

Live Application

The project is deployed as an interactive dashboard.

Live Demo:
[https://your-streamlit-link.streamlit.app](https://health-data-analytics-2fvqfom2fomzjkyn7w9si3.streamlit.app/)

Users can enter health parameters and receive real-time health risk predictions along with data visualizations.

Project Objective

The objective of this prototype is to:

Analyze health-related data

Perform exploratory data analysis

Train a machine learning model for risk prediction

Visualize relationships between health indicators

Provide real-time predictions through an interactive dashboard

This prototype demonstrates how data analytics and AI can assist digital health monitoring systems.

Dataset

A synthetic dataset of 100+ simulated patients was generated using Python.

Dataset Features
Feature	Description
patient_id	Unique identifier
age	Age of the patient
gender	Male / Female
heart_rate	Heart rate (beats per minute)
sleep_hours	Average daily sleep
daily_steps	Physical activity level
blood_pressure	Systolic blood pressure
stress_level	Stress score (1–10)
bmi	Body Mass Index
smoking_status	Smoking habit
exercise_frequency	Exercise level

The dataset simulates lifestyle and physiological health indicators commonly used in digital health systems.

Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed using:

Pandas

Matplotlib

Seaborn

The following analyses were conducted:

Summary statistics

Missing value check

Correlation analysis

Distribution of health indicators

Example visualizations include:

BMI distribution

Heart rate vs stress level

Daily steps vs risk level

Correlation heatmap

These visualizations help identify patterns and relationships in patient health data.

Machine Learning Model

A Random Forest Classifier was used to predict health risk levels.

Risk Categories

Low Risk

Medium Risk

High Risk

Why Random Forest?

Random Forest was selected because it:

Handles mixed numerical and categorical features

Reduces overfitting using ensemble learning

Performs well on classification tasks

The dataset was split into training and testing sets to evaluate model performance.

Interactive Dashboard

An interactive dashboard was built using Streamlit.

Dashboard Features

Real-time health data input

Machine learning based risk prediction

Patient dataset viewer

Health indicator visualizations

Data-driven insights

Users can enter new patient information such as:

heart rate

sleep hours

daily steps

BMI

smoking habit

exercise frequency

The system instantly predicts the health risk level.

Project Structure
health-data-analytics
│
├── dashboard
│   └── app.py
│
├── data
│   └── health_dataset.csv
│
├── model
│   └── risk_model.pkl
│
├── scripts
│   ├── generate_data.py
│   └── model.py
│
├── visualizations
│   ├── bmi_distribution.png
│   ├── heart_rate_vs_stress.png
│   └── steps_vs_risk.png
│
├── requirements.txt
└── README.md
Key Insights

The analysis revealed several important health patterns:

Patients with lower sleep hours tend to have higher stress levels.

Individuals with lower daily steps show higher predicted health risk.

Higher BMI values correlate with increased health risk.

Smoking combined with low physical activity increases risk probability.

Regular exercise is associated with healthier BMI and lower stress levels.

These insights demonstrate how health analytics systems can identify potential lifestyle-related health risks.

Technologies Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

Streamlit

Conclusion

This project demonstrates how health data analytics can transform raw patient data into meaningful insights. By combining machine learning, visualization, and interactive dashboards, the system simulates a simplified digital health monitoring platform capable of predicting potential health risks and supporting preventive healthcare decisions.
