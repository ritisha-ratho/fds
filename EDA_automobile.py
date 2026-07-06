import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("automobile.csv")
# Make Distribution
plt.figure(figsize=(8,5))
sns.countplot(x='make', data=df)
plt.title("Car Make Distribution")
plt.xticks(rotation=90)
plt.show()

# Fuel Type Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='fuel-type', data=df)
plt.title("Fuel Type Distribution")
plt.show()

# Body Style Distribution
plt.figure(figsize=(7,4))
sns.countplot(x='body-style', data=df)
plt.title("Body Style Distribution")
plt.show()

# Horsepower Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['horsepower'], bins=20, kde=True)
plt.title("Horsepower Distribution")
plt.show()

# Price Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['price'], bins=20, kde=True)
plt.title("Price Distribution")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Matrix")
plt.show()
