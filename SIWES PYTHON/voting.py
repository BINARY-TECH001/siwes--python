name = input("ENTER YOUR NAME : ")
age = int(input("ENTER YOUR AGE PLEASE: "))
if (age >= 18):
    print("congratulation !!! \n YOU ARE ELIGLE TO VOTE")
else:
    print("sorry!!! you are eligible to vote\n note: you must be 18years and above")
citizen = input("ARE YOU A CITIZEN OF NIGERIA ? ")
if (citizen == "yes"):
    print("congratulation mr/mrs {} you can vote".format(name))
else :
    print("sorry")
