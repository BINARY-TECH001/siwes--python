login = {
    "username" : "ademola",
    "password" : "password01"
    }

user_name = input("ENTER YOUR USERNAME: ")
pass_word = input("ENTER YOUR PASSWORD: ")
if user_name == login["username"] and pass_word == login["password"]:
    print(" LOGIN SUCCESSFUL ")
else:
    print("  INCORRECT USERNAME OR PASSWORD ") 