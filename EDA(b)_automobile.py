import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("automobile.csv")
# (b) Identify Attributes
print("\nNumeric Attributes")
numeric = df.select_dtypes(include=['int64','float64']).columns
print(numeric)

print("\nNominal Attributes")
nominal = ['num-of-doors','body-style']

print(nominal)

print("\nBinary Attributes")
binary = ['aspiration']

print(binary)
