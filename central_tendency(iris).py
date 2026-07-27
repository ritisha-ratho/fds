import pandas as pd

# Load the dataset
df = pd.read_csv("iris.csv")

# Check for null values
print("Null values in each column:")
print(df.isnull().sum())

# Replace null values with mean if any exist
if df.isnull().sum().sum() > 0:
    numeric_columns = df.select_dtypes(include=['number']).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    print("\nNull values replaced with column means.")
else:
    print("\nNo null values found.")

# Central Tendency
print("\nMean:")
print(df.select_dtypes(include=['number']).mean())

print("\nMedian:")
print(df.select_dtypes(include=['number']).median())

print("\nMode:")
print(df.mode().iloc[0])
