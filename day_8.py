from sklearn.linear_model import LinearRegression
import pandas as pd

# Sample dataset
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[["Hours"]]
y = df["Marks"]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict marks for 6 study hours
prediction = model.predict([[6]])

print("Predicted Marks for 6 Hours:", prediction[0])