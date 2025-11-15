import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import numpy as np

data={
      
      'Area': [650, 800, 1000, 1200, 1500, 1800, 2000, 2300, 2500, 2800],
      'Bedrooms': [1, 2, 2, 3, 3, 4, 3, 4, 4, 5],
      'Price': [70000, 85000, 100000, 110000, 150000, 165000, 170000, 200000,210000, 250000]
      
      }

df=pd.DataFrame(data)
df


x=df[["Area","Bedrooms"]]
x
y=df["Price"]
y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)

model1=LinearRegression()
model1.fit(x_train,y_train)

y_pred=model1.predict(x_test)


mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test, y_pred)
rmse=np.sqrt(mse)
r2=r2_score(y_test,y_pred)


print(f"mae:{mae:.2f}",mae)
print(f"mse{mse:.2f}",mse)
print(f"rmse{rmse:.2f}",rmse)
print(f"RSQR:{r2:.2f}",r2)

