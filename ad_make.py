
def dic():
    
    dictonary={
        "hk":"welcome hk",
        "ad":"welcome ad",
        "1":"thank you join me"
        
        
        }
    return dictonary



def res(user_input,data):
    
    user_input=user_input.lower().strip()
    
    if user_input in data:
        return data[user_input]
    




def main():
    
    while True:
        user_input=input("you:")
        
        data=dic()
    
    
        if user_input.lower().strip() =="1":
            print("Bot:",data["1"])
            break
    
        respond=res(user_input,data)
        print("replay:",respond)
    
    

if __name__ == "__main__":
    main()
    