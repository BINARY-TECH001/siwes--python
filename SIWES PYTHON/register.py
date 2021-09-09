login = {
    
    }
print("    welcome to my App \n    Register below\n")

login["username"] = input("ENTER YOUR USERNAME: ")
login["password"] = input("ENTER YOUR PASSWORD: ")

print("\nThanks for registering\nLogin to continue\n ")
user_name = input("ENTER YOUR USERNAME: ")
pass_word = input("ENTER YOUR PASSWORD: ")

if user_name == login["username"] and pass_word == login["password"]:
    print(" LOGIN SUCCESSFUL ")
else:
    print("  INCORRECT USERNAME OR PASSWORD ")