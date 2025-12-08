import numpy as np
from sklearn.linear_model import LinearRegression

# Data
X = np.array([[1], [2], [3], [4], [5]])  # hours
y = np.array([40, 50, 60, 70, 80])      # marks

# Model
model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction for 7 hours:", model.predict([[7]]))