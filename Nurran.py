import os

os.chdir("E:/ai")

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay

from sklearn.metrics import classification_report,accuracy_score
import matplotlib.pyplot as plt


df=pd.read_csv("weather_forecast_data_log.csv")
df

df_2=df


lblencoder=LabelEncoder()

df['Rain']=lblencoder.fit_transform(df["Rain"])

df

print(df)




x=df[["Temperature","Humidity","Wind_Speed","Cloud_Cover","Pressure"]]
x

y=df["Rain"]
y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)


len(x_train)

len(x_test)


scaler=StandardScaler()

x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)


mlp=MLPClassifier(hidden_layer_sizes=(12,12),activation="relu",solver="adam",max_iter=1000,random_state=0)

mlp.fit(x_train,y_train)

y_pred=mlp.predict(x_test)
y_pred


cm=confusion_matrix(y_test,y_pred)
cm

accuracy=accuracy_score(y_pred,y_test)

cr=classification_report(y_pred,y_test)

print(cr)


print("Accuracy",accuracy)

lblencoder.classes_


ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=lblencoder.classes_).plot(cmap=plt.cm.Blues)

plt.title("Confustion Matrix")
plt.plot()
