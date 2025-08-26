#NAN: NOT A NUMBER


import pandas as pd
df=pd.read_csv("ad1_26082025.csv")
print(df)
df.head(1)
df.tail(1)
df.info()
df.shape
df.describe()
df[['name','age','gpa']]
df.isnull().sum()   # give a blank of a avilabe in col

df.columns

for i in df.columns:
    print(i)

add_data=['Anand','aau','jau','','']
new=df.insert(loc=2,column="city",value=add_data)   

data=["IND","IND","PAK","",""]
df["State"]=data




