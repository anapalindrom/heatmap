import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'study_sessions.csv' 
df = pd.read_csv(file_path)

print(df.head())

print(df.dtypes)

df["Duration"] = pd.to_timedelta(df["Duration"], errors='coerce')

print(f'Number of NaT in Duration: {df["Duration"].isnull().sum()}')

df = df.dropna(subset=["Duration"])

df["Duration_in_hours"] = df["Duration"].dt.total_seconds() / 3600

study_duration = df.groupby(['Subject', 'Mood'])['Duration_in_hours'].sum().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
ax = sns.heatmap(study_duration, cmap='YlGnBu', annot=True, fmt='.2f', linewidths=0.5)

plt.title("Total Study Duration by Subject and Mood", fontsize=14)
plt.xlabel("Mood", fontsize=12)
plt.ylabel("Subject", fontsize=12)

colorbar = ax.collections[0].colorbar
colorbar.ax.set_position([0.9, 0.1, 0.02, 0.8]) 

plt.tight_layout()
plt.show()
