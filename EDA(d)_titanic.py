import sys
print(sys.executable)

import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

# Read Titanic dataset
df = pd.read_csv("titanic.csv")

# Select numeric attributes
temp = df[['Age', 'Fare']].dropna()

# Calculate Euclidean distance between first two passengers
distance = euclidean_distances([temp.iloc[0]], [temp.iloc[1]])

print("Euclidean Distance:")
print(distance)
