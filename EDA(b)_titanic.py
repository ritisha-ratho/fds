import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Titanic.csv")
# (b) Identify Attributes
print("\nNumeric Attributes")
numeric = df.select_dtypes(include=['int64','float64']).columns
print(numeric)

print("\nNominal Attributes")
nominal = ['Sex','Embarked']

print(nominal)

print("\nBinary Attributes")
binary = ['Survived']

print(binary)
