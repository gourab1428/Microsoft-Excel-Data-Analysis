import pandas as pd 
df = pd.read_csv("SQL_Sales_Dataset.csv")
print(df. head())
print(df.info())
print(df.shape)

print("\n Missing Value")
print(df.isnull().sum())
print("\nDuplicate rows")
print(df.duplicated().sum())
df=df.drop_duplicates()
print("\nShape after removing duplicates")
print(df.shape)
# Calculate total revenue by category
category_revenue = df.groupby("category")["total_price"].sum()

category_revenue = df.groupby("category")["total_price"].sum()
print("\nTotal Revenue by Category:")
print(category_revenue)

sorted_data = df.sort_values(
    by=["category","total_price"],
    ascending=[True,False]
)

print("\nSorted Data: ")
print(sorted_data.head(10))

correlation_matrix = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(correlation_matrix)