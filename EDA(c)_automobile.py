import pandas as pd

# Load the dataset
df = pd.read_csv("automobile.csv")

# Select two nominal attributes
attr1 = "fuel-type"
attr2 = "body-style"

# Calculate dissimilarity for each record
dissimilarity = []

for i in range(len(df)):
    if df[attr1][i] == df[attr2][i]:
        dissimilarity.append(0)
    else:
        dissimilarity.append(1)

df["Nominal_Dissimilarity"] = dissimilarity

print(df[[attr1, attr2, "Nominal_Dissimilarity"]].head(10))
