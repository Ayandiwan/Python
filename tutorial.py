
later='''

hello |name|
good morning sir
How are you
what is  give |date|'''

print(later.replace("|name|", "Ayan").replace("|date|", "18-7-2025"))

var="AyanDiwan  at khdana"

print(var.find("  "))  # fine double space indax value



latere='''

hello how are you 


'''
print(latere.replace(" ", "1"))



#_____________List_________

frute=["Ayan","Diwan",1,2,11,True]
print(frute)

print(type(frute))
print(frute[5])

print(frute.append("jadu"))
print(frute)

num=[5,4,3,2,1]
sor=num.sort()
print(num)

rev=[5,4,3,2,1]
rev=rev.reverse()
print(rev)

#   is dis  avilable key and value




data={
      "item1":(1,2,(1,1)),
      "item2":(3,4,(5,5)),#  first key and second is value
      "item3":(5,6,(7,7))  
      }


print(data)
print(data["item1"][0])



stu={
     "sem":("ayan","diwan",("hk","khan")),
     "Age":(20,25,(4))     
     }

print(stu["Age"][2])


list_1=[1,2,3,4,5,6]
print(list_1)

list_1.remove(2)


#________tuple____

#_is a inmutable

a=(1)  # not a tuple for one element
print(type(a))


a=(1,) # this is a tuple
print(type(a))



def ad(a,b):
    c=a+b
    print("anser:",c)


ad(7,8)


# enter the user enter in list to store

ad=[]

for i in range(0,6):
    f1=int(input("Enter your Number"))
    ad.append(f1)

print(ad)

ad.clear()
ans=ad.sort()
print(ans)
        

#_____________________dictonary_____________

dic={
     "name":"ayan",
     "sem":5,
     "RollNo:":7,
     "Regno":"3060823008"
     
     }

print(dic.items())

dic.update({"name":"adking","hk":"noob"})   # here hk is not in dis but the authmoticaly add
print(dic)

dic.get("name")   # rturn the value



#_____________sets_____________

s={1,2,3,3}  # not are avilabe in key and value

# not allowd the repete element

print(type(s))

e=set()#  crate a empty set 
num=int(input("Enter No::"))


for i in range(0,6):
    num=int(input("Enter No::"))
    e.add(num)

e.clear()

print(type(e))

s.add(7)

s.remove(3)
s

s.pop()  # first element are removed

s1={1,2,3,4}
s2={4,5,6,7}  #  not repete 4 in only a one tim

print(s1.union(s2))
print(s1.intersection(s2))  # comon value give
print(s1.difference(s2))  # 1,2,3

print(s1.issubset(s2))



dic={
     "ad":"ayan",
     "fan":"msd"
     }

word=input("Enter Your Words:")

print(dic[word])

# print Unike No: 
s=set()

for i in range(0,8):
    n=int(input("enter Your Number:"))
    s.add(n)
    
print(s)

s.clear()


#  add intreactive 

dis1={}

key=input("Enter Key:")
val=input("Enter val:")

dis1.update({key, val})

dis1


#______check_____________


post=input("enter your name:")

if("Ayan".lower() in post.lower()):
    print("done")

else:
    print("sorry")









#_______prime no_____


    
num=int(input("Enter Your No:"))

if num < 2:
    print("Not a prirm or composite")

else:
    for i in range(2,num):
        if num % i == 0:
            print("Composite No")
            break
        
    else:
        print("Prime No")


