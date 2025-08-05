#_______for loop_________


for i in range(0,7):
    print(i)
else:
    print("for is over")
#__________while loop_____



list=["hello",1,2,3,4,"ayan","kjj"]

i=0
while (i<len(list)):
    print(list[i])
    
    i=i+1
    
for i in range(101):
    pass

i=1
while i<1099:
    print(i)
    i=i+1
    
# multification NO
n=int(input("Enter your Number:"))
for i in range(1,11):
    print(f"{n} * {i}={n*i}")

lis=["ayan","ad","hk","jk","a"]


for i in lis:
    if i.startswith("a"):
        print(i)
        
        
        
        
#  Prime No


num=int(input("Enter your Number:"))

for i in range(2,num):
    if num % i == 0:
        print("Composite No")
        break
        
else:
    print("Prime No")


#_________sum


num=int(input("Enter your Number:"))

i=1
sum=0

while i <= num:
    sum =sum+i
    i=i+1
print(sum)


      