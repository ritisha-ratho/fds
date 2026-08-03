import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")   

numeric_df = df.select_dtypes(include=['number'])

numeric_df = numeric_df.fillna(numeric_df.mean())

print("Range:")
print(numeric_df.max() - numeric_df.min())
print("\nVariance:")
print(numeric_df.var())
print("\nStandard Deviation:")
print(numeric_df.std())
print("\nInterquartile Range (IQR):")
Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

# Histogram
numeric_df.hist(figsize=(12, 8), bins=20)
plt.suptitle("Histograms of Titanic Dataset")
plt.show()

# Box Plot
plt.figure(figsize=(12, 6))
numeric_df.boxplot()
plt.title("Box Plot of Titanic Dataset")
plt.xticks(rotation=45)
plt.show()
