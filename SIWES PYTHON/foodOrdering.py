print("WELCOME TO ADEMOLA KITCHEN")
about = {
    "ABOUT US" : "ADEMOLA KITCHEN is a kitchen own and directed by ADEMOLA INVESTMENT NIG LTD. it is first off its kind in the field , the kichen is with qualified and experienced chef under supervision and management. \n      YOUR SATISFACTION IS OUR CONCERN. "
    
    }

kitchen_address = {
    "address" : "no.12, kola sanusi street mabolaje area oyo",
    "phone_Number" : "09059343602"
    }
food_list = {
    "localfoods" : [ "amala" ,"pounded yam ","semo"],
    "foreign_foods" : ["pizza","shawarma","rice"],
    
     }
name =  input("ENTER YOUR NAME PLEASE: ")
name = name.upper()
action1 = print(" 1. kitchen address and phone number")
action2 = print(" 2. check available food")
action3 = print(" 3. about ADEMOLA KITCHEN")
User_input = input("DEAR {}, SELECT ANY ACTION OF YOUR CHOICCE:   ".format(name))

if User_input == "1":
    print(kitchen_address)
elif User_input == "2" :
    print(food_list)
elif User_input == "3" :
    print(about)
    
    
else:
   print("WRONG INPUT")    

print("DEAR {}, THANKS FOR CONTACTING ADEMOLA KITCHEN  ".format(name))