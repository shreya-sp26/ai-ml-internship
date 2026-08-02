from sklearn.linear_model import LinearRegression
import pandas as pd

# Sample dataset
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Hours"]]
y = df["Marks"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# User input
hours = float(input("Enter study hours: "))

# Predict score
predicted_score = model.predict([[hours]])

print("Predicted Score:", predicted_score[0])