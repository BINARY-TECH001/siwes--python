login = {
    
    }
print("    welcome to NACOSS ELECTORAL COMMISSION. \n    Register below\n")

login["name"] = input("ENTER YOUR FULLNAME: ")
login["age"] = input("ENTER YOUR AGE: ")
login["sex"] = input("SEX: ")
login["matricNo"] = input("ENTER YOUR MATRIC-NO: ")
login["department"] = input("ENTER YOUR DEPAARTMENT: ")
login["level"] = input("ENTER YOUR LEVEL: ")


print("\nThanks for registering\nLogin to continue\n ")
name = input("ENTER YOUR FULLNAME: ")
age = input("ENTER YOUR AGE: ")
sex = input("ENTER YOUR SEX: ")
matricNo = input("ENTER YOUR MATRIC-NO: ")
department = input("ENTER YOUR DEPARTMENT: ")
level = input("ENTER YOUR LEVEL: ")


if name == login["name"] and age == login["age"] and sex == login["sex"] and matricNo == login["matricNo"] and department == login["department"] and level == login["level"]:
    print(" LOGIN SUCCESSFUL \n you are eligible to vote")
else: 
    print("  SORRY, YOU ARE NOT ELIGIBLE TO VOTE \n   try agin later..... ") 