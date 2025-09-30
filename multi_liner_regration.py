from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression

df = pd.read_csv("mlr.csv")
print(df)

df.columns
print(df)

df.columns = df.columns.str.strip() 

df.columns
print(df)

df.corr()
print(df)

df1 = df[['Years of Experience','Education Level', 'Number of Certifications', 'Hobby Score', 'Salary']]
print(df1)

df1.corr()

x = df1[['Years of Experience','Education Level','Number of Certifications','Hobby Score']]
print(x)

Y = df1['Salary']
print(Y)

print(df1.shape)
print(x.shape)
print(Y.shape)

multlm = LinearRegression()
x

multlm.fit(x,Y)

b = multlm.coef_
print(b)

b0 = multlm.intercept_
print(b0)

d = np.array([[29,20,11,8]])
p = multlm.predict(d)
print(p)


p1 = b0 + np.dot(b,d.ravel())
print(p1)








