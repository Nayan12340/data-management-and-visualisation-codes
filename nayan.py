import pandas as pd
import numpy as np


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", None],
    "Age": [25, np.nan, 30, 35, 28],
    "Salary": [50000, 60000, np.nan, 80000, 75000],
    "Department": ["HR", "IT", None, "Finance", "IT"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")


print("Missing values in each column:")
print(df.isnull().sum())
print("\n")


df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())


df["Department"] = df["Department"].fillna("Unknown")


df = df.dropna(subset=["Name"])

print("DataFrame after handling missing values:")
print(df)
print("\n")


print("Remaining missing values:")
print(df.isnull().sum())