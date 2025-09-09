import pandas as pd
import os

os.chdir("e:\SEM_5\python")

df=pd.read_csv("students_gujarat.csv")
df

print(df["Age"])
df.iloc[:,0]
df.iloc[:,1]
df.iloc[:,0:2]
df.iloc[0:6,0:4]

#Find Mean

mean_age=df["Age"].mean()
mean_age

median_age=df["Age"].median()
median_age

mode_age=df["Age"].mode()
mode_age


df.isna()
null_counts = df.isna().sum()
null_counts

columns_null = null_counts[null_counts > 0]
columns_null

df

mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)



df = pd.read_csv('students_gujarat.csv')
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)
df



df = pd.read_csv('students_gujarat.csv')
mod_age = df['Age'].median()
df['Age'] = df['Age'].fillna(mod_age)
df


df = pd.read_csv('students_gujarat.csv')
df['Age'] = df['Age'].fillna(18)
df


df = pd.read_csv('students_gujarat.csv')
df

df_dropped = df.dropna()  # Null value is delete
df_dropped
















