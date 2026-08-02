from sklearn.linear_model import LinearRegression
import pandas as pd

# Student study hours and marks dataset
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Select input and output
X = df[["Hours"]]
y = df["Marks"]

# Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Get user input
hours = float(input("Enter study hours: "))

# Predict score
predicted_score = model.predict([[hours]])

# Display result
print("Predicted Score:", predicted_score[0])