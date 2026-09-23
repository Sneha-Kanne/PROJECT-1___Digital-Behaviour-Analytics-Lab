import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("placement_readiness.csv")

python_scores = np.array(df["Python_Score"])
sql_scores = np.array(df["SQL_Score"])
aptitude_scores = np.array(df["Aptitude_Score"])
communication_scores = np.array(df["Communication_Score"])

average_python = np.mean(python_scores)
highest_aptitude = np.max(aptitude_scores)
lowest_aptitude = np.min(aptitude_scores)
communication_above_70 = np.sum(communication_scores > 70)

skill_scores = np.column_stack(
    (python_scores, sql_scores, aptitude_scores, communication_scores)
)

skill_gap = np.max(skill_scores, axis=1) - np.min(skill_scores, axis=1)

print("Average Python Score:", average_python)
print("Highest Aptitude Score:", highest_aptitude)
print("Lowest Aptitude Score:", lowest_aptitude)
print("Students above 70 in Communication:", communication_above_70)
print("Skill Gap for each student:", skill_gap)

print("\nFirst 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDescription:")
print(df.describe())

print("\nStudents with Python Score above 75:")
print(df[df["Python_Score"] > 75])

print("\nStudents sorted by Aptitude Score:")
print(df.sort_values("Aptitude_Score", ascending=False))

print("\nTop 10 students by Python Score:")
print(df.sort_values("Python_Score", ascending=False).head(10))

print("\nStudents strong in Python but weak in Communication:")
print(
    df[
        (df["Python_Score"] > 75)
        & (df["Communication_Score"] < 60)
    ]
)

df["Total_Score"] = (
    df["Python_Score"]
    + df["SQL_Score"]
    + df["Aptitude_Score"]
    + df["Communication_Score"]
)

df["Average_Score"] = df["Total_Score"] / 4

df["Weakest_Skill_Score"] = df[
    ["Python_Score", "SQL_Score", "Aptitude_Score", "Communication_Score"]
].min(axis=1)

df["Readiness_Score"] = (
    df["Average_Score"]
    + (df["Projects_Completed"] * 2)
    + df["Mock_Interviews_Attended"]
).clip(upper=100)

df["Readiness_Band"] = np.select(
    [
        df["Readiness_Score"] >= 75,
        df["Readiness_Score"] >= 60
    ],
    [
        "Ready",
        "Almost Ready"
    ],
    default="Needs Work"
)

print("\nReadiness Band Counts:")
print(df["Readiness_Band"].value_counts())

print("\nLargest Readiness Band:")
print(df["Readiness_Band"].value_counts().idxmax())

df.to_csv("placement_results.csv", index=False)

import os

os.makedirs("charts", exist_ok=True)

skill_averages = [
    df["Python_Score"].mean(),
    df["SQL_Score"].mean(),
    df["Aptitude_Score"].mean(),
    df["Communication_Score"].mean()
]

skills = [
    "Python",
    "SQL",
    "Aptitude",
    "Communication"
]

plt.figure(figsize=(8, 5))
plt.bar(skills, skill_averages)
plt.title("Average Score for Each Skill")
plt.xlabel("Skills")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("charts/skill_comparison.png")
plt.close()

band_counts = df["Readiness_Band"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(band_counts.index, band_counts.values)
plt.title("Students in Each Readiness Band")
plt.xlabel("Readiness Band")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("charts/readiness_bands.png")
plt.close()

branch_readiness = df.groupby("Branch")["Readiness_Score"].mean()

plt.figure(figsize=(8, 5))
plt.bar(branch_readiness.index, branch_readiness.values)
plt.title("Average Readiness Score by Branch")
plt.xlabel("Branch")
plt.ylabel("Average Readiness Score")
plt.tight_layout()
plt.savefig("charts/branch_readiness.png")
plt.close()

print("\nplacement_results.csv created successfully.")
print("Three charts saved in the charts folder.")