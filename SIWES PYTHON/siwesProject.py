score = 0
score = int(score)
name = input("ENTER YOUR NAME PLEASE: ")
name = name.upper()
print("    WELCOME {} ".format(name))
print("PLEASE ANSWER BY TYPING a or b (LOWER CASE PLEASE)")
question1 =input ("Q1. WHAT IS THE NAME OF THE PRESIDENT OF NIGERIA? \n a. yemi osinbajo \n b. muhammed buhari \n c. Goodluck ebele jonathan \n d. isiaq abiola ajimobi \n ")
answer1 = "b"
response1 = input("ANSWER: ")
if answer1 == response1:
    print("welldone "  + response1 +  " is correct")
else:
    print("sorry,that is not correct")
score = score + 1


question2 = input("Q2. ONE VERY IMPORTANT ASPECT OF HUMAN RELATIONSHIP IS _________TRUST \n a. communal \n b. individual \n c. mutual \n d. personal \n ")
answer2 = "c"
response2 = input("ANSWER: ")
if answer2 == response2:
    print("welldone "  + response2 +  " is correct")
else:
    print("sorry,that is not correct")
score = score + 1

question3 = input("Q3. THE TWO TASK WERE PERFORMED _______AND WE WERE ABLE TO FINISH EARLY. \n a. alternatively \n b. simultaneously \n c. consecutively \n d. separately \n ")
answer3 = "b"
response3 = input("ANSWER: ")
if answer3 == response1:
    print("welldone "  + response3 +  " is correct")
else:
    print("sorry,that is not correct")
score = score + 1

question4 = input("Q4. THERE ARE ________STATES IN NIGERIA . \n a. 40 \n b. 33 \n c. 36 \n d. 34 \n ")
answer4 = "c"
response4 = input("ANSWER: ")
if answer4 == response4:
    print("welldone "  + response4 +  " is correct")
else:
    print("sorry,that is not correct")
score = score + 1
print("YOUR SCORE IS : " + str(score))