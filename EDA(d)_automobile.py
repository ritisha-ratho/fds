import sys
print(sys.executable)

import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

df = pd.read_csv("automobile.csv")


df.replace("?", pd.NA, inplace=True)


df["engine-size"] = pd.to_numeric(df["engine-size"], errors="coerce")
df["horsepower"] = pd.to_numeric(df["horsepower"], errors="coerce")


temp = df[["engine-size", "horsepower"]].dropna()

distance = euclidean_distances([temp.iloc[0]], [temp.iloc[1]])

print("Euclidean Distance:")
print(distance)
