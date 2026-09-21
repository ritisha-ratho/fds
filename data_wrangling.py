import pandas as pd
# Load Titanic dataset
df = pd.read_csv("titanic.csv")
print("----- FIRST 5 ROWS -----")
print(df.head())
# 1. CREATE DATAFRAME
data = {
    "Name": ["John", "Alice", "Robert"],
    "Age": [25, 30, 40],
    "Sex": ["male", "female", "male"]
}
new_df = pd.DataFrame(data)
print("\n----- CREATED DATAFRAME -----")
print(new_df)
# 2. SELECT COLUMNS
print("\n----- SELECTED COLUMNS -----")
print(df[["Name", "Age", "Sex"]].head())

# 3. FILTERING
print("\n----- FEMALE PASSENGERS -----")
print(df[df["Sex"] == "female"].head())
# 4. HIERARCHICAL INDEXING
multi_df = df.set_index(["Sex", "Pclass"])

print("\n----- HIERARCHICAL INDEX -----")
print(multi_df.head())
# 5. CONCATENATION
df1 = df.head(5)
df2 = df.tail(5)
concat_df = pd.concat([df1, df2])
print("\n----- CONCATENATED DATAFRAME -----")
print(concat_df)
# 6. MERGING
passenger = df[["PassengerId", "Name", "Pclass"]].head(10)

survival = df[["PassengerId", "Survived"]].head(10)

merged_df = pd.merge(
    passenger,
    survival,
    on="PassengerId"
)
print("\n----- MERGED DATAFRAME -----")
print(merged_df)
# 7. COMBINING

df_a = pd.DataFrame({
    "Age": [22, None, 35],
    "Fare": [7.25, 71.28, None]
})

df_b = pd.DataFrame({
    "Age": [25, 30, 40],
    "Fare": [10.0, 70.0, 20.0]
})

combined_df = df_a.combine_first(df_b)

print("\n----- COMBINED DATAFRAME -----")
print(combined_df)

# 8. RESHAPING USING MELT
small_df = df[
    ["PassengerId", "Age", "Fare"]
].head(5)

melted_df = pd.melt(
    small_df,
    id_vars=["PassengerId"],
    value_vars=["Age", "Fare"],
    var_name="Variable",
    value_name="Value"
)

print("\n----- MELTED DATAFRAME -----")
print(melted_df)

# 9. PIVOT TABLE
pivot_df = pd.pivot_table(
    df,
    values="Survived",
    index="Sex",
    columns="Pclass",
    aggfunc="mean"
)

print("\n----- PIVOT TABLE -----")
print(pivot_df)
# 10. GROUPBY
print("\n----- SURVIVAL RATE BY SEX -----")

group_df = df.groupby("Sex")["Survived"].mean()

print(group_df)
# 11. SORTING

sorted_df = df.sort_values(
    by="Fare",
    ascending=False
)

print("\n----- SORTED BY FARE -----")
print(sorted_df.head(10))

# 12. MISSING VALUES
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

