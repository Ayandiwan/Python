import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Dataset
data = {
 'Area': [650, 800, 1000, 1200, 1500, 1800, 2000, 2300, 2500, 2800],
 'Bedrooms': [1, 2, 2, 3, 3, 4, 3, 4, 4, 5],
 'Price': [70000, 85000, 100000, 110000, 150000, 165000, 170000, 200000,
           210000, 250000]
}

df = pd.DataFrame(data)
print(df)

# Data split
X = df[['Area', 'Bedrooms']]  # Independent variables
y = df['Price']               # Dependent variable

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model fit
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Adjusted R-squared (avoid ZeroDivisionError)
n = X_test.shape[0]  # number of samples
p = X_test.shape[1]  # number of predictors

if n > p + 1:
    adj_r2 = 1 - (1 - r2) * ((n - 1) / (n - p - 1))
else:
    adj_r2 = None  # Not enough samples

# Display results
print("\nModel Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared: {r2:.4f}")

if adj_r2 is not None:
    print(f"Adjusted R-squared: {adj_r2:.4f}")
else:
    print("Adjusted R-squared: Not enough samples to calculate.")
