import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/health_dataset.csv")

print("Summary Statistics")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="coolwarm")
plt.title("Feature Correlation")
plt.show()