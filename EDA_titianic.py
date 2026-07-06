import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Exploratory Data Analysis (EDA)
# Survival Count
df = pd.read_csv("Titanic.csv")
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

# Gender Count
sns.countplot(x='Sex', data=df)
plt.title("Gender Distribution")
plt.show()

# Passenger Class
sns.countplot(x='Pclass', data=df)
plt.title("Passenger Class")
plt.show()

# Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

# Fare Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Fare'], bins=20, kde=True)
plt.title("Fare Distribution")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Matrix")
plt.show()

