name = input("ENTER YOUR NAME PLEASE: ")
name = name.upper()
print("    WELCOME {} ".format(name))
print("PLEASE ANSWER BY TYPING a or b (LOWER CASE PLEASE)")
question1 = input("Q1. WHAT IS THE NAME OF THE PRESIDENT OF NIGERIA? \n a. yemi osinbajo \n b. muhammed buhari \n c. Goodluck ebele jonathan \n d. isiaq abiola ajimobi \n ")
while question1 == "b":
   break
question2 = input("Q2. ONE VERY IMPORTANT ASPECT OF HUMAN RELATIONSHIP IS _________TRUST \n a. communal \n b. individual \n c. mutual \n d. personal \n ")
while question2 == "c":
    break
question3 = input("Q3. THE TWO TASK WERE PERFORMED _______AND WE WERE ABLE TO FINISH EARLY. \n a. alternatively \n b. simultaneously \n c. consecutively \n d. separately \n ")
while question3 == "b":
   break
question4 = input("Q4. THERE ARE ________STATES IN NIGERIA . \n a. 40 \n b. 33 \n c. 36 \n d. 34 \n ")
while question4 == "c":
   break
if question1 == "b" and question2 == "c" and question3 == "b" and question4 =="c":
    print("EXCELLENT")

else:
    print("FAIL")