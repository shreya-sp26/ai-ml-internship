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

# Predict student scores
study_hours = [[2.5], [4], [6]]
predictions = model.predict(study_hours)

for hour, score in zip(study_hours, predictions):
    print(f"Study Hours: {hour[0]}, Predicted Score: {score:.2f}")