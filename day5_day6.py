import pandas as pd
import matplotlib.pyplot as plt

# Create sample dataset
data = {
    "Name": ["Shreya", "Rahul", "Priya", "Rahul"],
    "Marks": [85, 90, None, 90]
}

df = pd.DataFrame(data)

# Handle missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicates
df = df.drop_duplicates()

# Dataset statistics
print(df.describe())

# Bar Chart
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.show()

# Line Chart
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Student Marks")
plt.show()

# Scatter Plot
plt.scatter(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.show()