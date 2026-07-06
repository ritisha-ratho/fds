import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# (a) Read the Dataset
df = pd.read_csv("automobile.csv")

print("First 5 Records")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nStatistical Summary")
print(df.describe())

