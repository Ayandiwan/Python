import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd 

data_set= pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Soil Fertility data.csv') 

#Extracting Independent Variable
x= data_set.iloc[:, :-1].values
print(x)


#Extracting Dependent variable
y= data_set.iloc[:, -1].values
print(y)

print(x)
print(y)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
model=scaler.fit(x)
scaled_data=model.transform(x)

print(scaled_data)