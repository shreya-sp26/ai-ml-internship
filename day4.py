import pandas as pd

# Create a sample student score dataset
data = {
    "Name": ["Shreya", "Heni", "Priya", "Amit"],
    "Score": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

# Display dataset
print(df)

# Display first rows
print("\nFirst 5 Rows:")
print(df.head())

# Display columns
print("\nColumns:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
print(df.info())