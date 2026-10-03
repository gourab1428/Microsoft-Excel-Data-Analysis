import pandas as pd

df = pd.read_csv("data.csv")
print("orginal dataset:")
print(df.head())

print("\nOrginal Shape")
print(df.shape)


print("Missing value:")
print(df.isnull().sum())


df["Date"] = pd.to_datetime(
    df["Date"].astype(str).str.replace("'",""),
    errors="coerce"
)

df = df.dropna(subset=["Date"])

df["Calories"] = df["Calories"].fillna(df["Calories"].median())

print("\n Missing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows Before Removing:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDuplicate Rows After Removing:")
print(df.duplicated().sum())

high_pulse = df[df["Pulse"] > 100]

print("\nRows Where Pulse > 100:")
print(high_pulse)


long_workouts = df[df["Duration"] >= 60]

print("\nWorkouts With Duration >= 60 Minutes:")
print(long_workouts)


df["Calories_Per_Minute"] = df["Calories"] / df["Duration"]


df["Pulse_Category"] = df["Pulse"].apply(
    lambda x: "High" if x >= 100 else "Normal"
)

print("\nDataset With New Columns:")
print(df.head())

df = df.sort_values(
    by="Calories",
    ascending=False
)

print("\nSorted By Calories:")
print(df.head(10))

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_data.csv")

print("\nFinal Shape:")
print(df.shape)