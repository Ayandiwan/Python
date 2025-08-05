#___________ Searching___________

dis=[
     
     {"id":"1","Name":"Ayan","Surname":"Diwan","Gpa":"6.85"},
     {"id":"2","Name":"HK","Surname":"Khan","Gpa":"7,11"},
     {"id":"3","Name":"MD","Surname":"Diwan","Gpa":"5.55"},
    
     ]

uid=input("Enter User Id:")
     
for i in dis:
    if i["id"]==uid:
        print("Id:",i["id"])
        print("Name:",i["Name"])
        print("Surname:",i["Surname"])
        print("Gpa:",i["Gpa"])

     
     
    