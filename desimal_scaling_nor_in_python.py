import statisticss
import pandas as pd

def decNor(num,maxNum):
 digit=len(str(maxNum))
 div=pow(10,digit)
 return num/div

data=[200, 300, 400, 600, 1000]
print(data)

num=int(input("Enter an item from data : \t"))

print("\nCalculating decimal scaling normalization")
print("After doing decimal scaling normalization : \t", decNor(num,max(data)))