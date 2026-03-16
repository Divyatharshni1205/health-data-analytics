import pandas as pd
import numpy as np

np.random.seed(42)
n = 120

data = {
    "patient_id": range(1, n+1),
    "age": np.random.randint(20,65,n),
    "gender": np.random.choice(["Male","Female"],n),
    "heart_rate": np.random.randint(60,100,n),
    "sleep_hours": np.round(np.random.uniform(4,9,n),1),
    "daily_steps": np.random.randint(2000,15000,n),
    "blood_pressure": np.random.randint(100,150,n),
    "stress_level": np.random.randint(1,10,n),
    "bmi": np.round(np.random.uniform(18,35,n),1),
    "smoking_status": np.random.choice(["Yes","No"],n),
    "exercise_frequency": np.random.choice(
        ["None","Low","Moderate","High"],n
    )
}

df = pd.DataFrame(data)

df.to_csv("data/health_dataset.csv",index=False)

print("Dataset created successfully")