from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression

df = pd.read_csv("slr.csv",)

df

df.corr()
x = df[['Years of Experience']]
print(x)

Y = df['Salary']
print(Y)

plt.scatter(x,Y)
plt.grid()
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Y vs. x ")

model1 = LinearRegression()

model1.fit(x,Y)
print(model1)

p1 = model1.predict([[30]])
print(p1)

