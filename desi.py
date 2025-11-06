import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_csv("mlr.csv")
df.columns = df.columns.str.strip()


x = df[["Years of Experience", "Education Level", "Number of Certifications", "Hobby Score"]]

y = df["Salary"]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)

print("Training Data:", x_train.shape)
print("Testing Data:", x_test.shape)


model = LinearRegression()
model.fit(x_train, y_train)


y_pred = model.predict(x_test)

result = pd.DataFrame({"Actual Salary": y_test, "Predicted Salary": y_pred})
print(result)

from sklearn.metrics import r2_score
print("R² Score =", r2_score(y_test, y_pred)*100)
