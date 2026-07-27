from sklearn.model_selection import train_test_split
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

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

print("Actual Marks:", list(y_test))
print("Predicted Marks:", prediction)