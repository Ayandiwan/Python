import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression


df = pd.read_csv("house.csv")
df
df.columns=df.columns.str.strip()    
df.columns


x = df[['Age','Income','CreditScore',]] 
Y = df['Purchased']


print(x)
print(Y)


logModel = LogisticRegression()

logModel.fit(x,Y)


yp = logModel.predict([[22,25000,500]])
print("Purchased:",yp)


b1 = logModel.coef_
print("coefficient:",b1)

b0 = logModel.intercept_
print("Intercept:",b0)

'''
[(22,25000,500)]*logModel.coef_ + logModel.intercept_

Yp = [(22,25000,500)]*logModel.coef_ + logModel.intercept_

print("predicted Y:",Yp)


1/(1+np.exp(-28.06956653))
Yp
'''


arr=np.array([22,25000,500])
Yp=np.dot(arr,b1.T) + b0
print("predicted Y",Yp)


SYp = 1/(1+np.exp(-Yp))
print("Sigmoid",SYp)

Ytmp = [Y,np.round(SYp)]
Ytmp

