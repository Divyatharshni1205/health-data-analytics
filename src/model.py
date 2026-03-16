import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle
import os



df = pd.read_csv("data/health_dataset.csv")

print("Dataset Loaded Successfully")
print(df.head())



def calculate_risk(row):

    score = 0

  
    if row["bmi"] > 30:
        score += 2
    elif row["bmi"] > 25:
        score += 1


    if row["daily_steps"] < 4000:
        score += 2
    elif row["daily_steps"] < 7000:
        score += 1

    
    if row["sleep_hours"] < 6:
        score += 1

    
    if row["stress_level"] > 7:
        score += 2
    elif row["stress_level"] > 5:
        score += 1

  
    if row["smoking_status"] == "Yes":
        score += 1

  
    if score >= 5:
        return "High"
    elif score >= 3:
        return "Medium"
    else:
        return "Low"


df["risk_level"] = df.apply(calculate_risk, axis=1)

print("\nRisk levels generated successfully")
print(df["risk_level"].value_counts())



encoders = {}

categorical_cols = ["gender", "smoking_status", "exercise_frequency"]

for col in categorical_cols:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])
    encoders[col] = encoder


target_encoder = LabelEncoder()
df["risk_level"] = target_encoder.fit_transform(df["risk_level"])



X = df.drop(["patient_id", "risk_level"], axis=1)
y = df["risk_level"]



X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))



model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Training Completed")


predictions = model.predict(X_test)

print("\nModel Evaluation Report:")
print(classification_report(y_test, predictions))



os.makedirs("model", exist_ok=True)

pickle.dump(model, open("model/risk_model.pkl", "wb"))

print("\nModel saved successfully at model/risk_model.pkl")