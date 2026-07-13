import pandas as pd

df = pd.read_csv("titanic.csv") 
row1 = df.loc[0, ['Sex', 'Embarked']]
row2 = df.loc[1, ['Sex', 'Embarked']]

print("Passenger 1:")
print(row1)

print("\nPassenger 2:")
print(row2)

# Calculate simple matching dissimilarity
dissimilarity = sum(row1 != row2)

print("\nNominal Dissimilarity =", dissimilarity)

