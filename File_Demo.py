




def load_dict():
    
    f = open("ad.txt","r")
    dict1 = {}
    
    for line in f:
        (key, value) = line.replace("\n","").split(":",1)
        dict1[key] = value
        
    return dict1    



def load_dict2():
    
    f = open("fruite.txt","r")
    dict2 = {}
    
    for line in f:
        (key, value) = line.replace("\n","").split(":",1)
        dict2[key] = value
        
    return dict2    




def respond(user_input, data):
    user_input = user_input.lower().strip()
    
    #data=load_dict()


    if user_input in data:
        return data[user_input]
    
    return "sorry not a understand"

def respond1(user_input, data):
    user_input = user_input.lower().strip()
    
    #data=load_dict()


    if user_input in data:
        return data[user_input]
    
    return "sorry not a understand lala"


# Fallback response
    

def main():
    print("Welcome to Bot ")
    print("(1)Name")
    print("(2)Fruite")
    print("Type 'exit' to quit.\n")
    
    data=load_dict()
    data1=load_dict2()


    
    while True:
        print("(1)Name")
        print("(2)Fruite")
        print("Type 'exit' to quit.\n")
        choice=input("Enter Your choice:")

        if choice == "1":
            while True:
                user_input = input("You: ")
                reply = respond(user_input, data)
                print("Bot:", reply)
                
                if user_input =="exit":
                    break
               
            
        elif choice == "2":
            while True:
                
                user_input = input("You: ")
                if user_input =="exit":
                    print("thank you for using ... \n")
                    break
                reply = respond1(user_input, data1)
                print("Bot:", reply)
                
                
                
              
        
        else:
            print("Invalid a Choice")
            
               
        
if __name__ == "__main__":
    main()        
    
    



  