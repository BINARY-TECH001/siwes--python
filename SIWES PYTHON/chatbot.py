name = input(" YOUR NAME PLEASE: ")
name = name.upper()

for i in range (0,20):
    user = input("RECEIVER: ")
    user = user.lower()
    
    if ("rain" in user):
        print("dear {},it is raining,Don't forget to go out with an umbrella".format(name))
    elif ("you doing" in user):
         print("{}: fine and you?".format(name))
    elif ("school" in user):
        print("{}: FCAHPTIB".format(name))
    elif ("your family doing" in user):
         print("{}: they are fine and yours?".format(name))
    elif ("fine" in user):
         print("{}: alright".format(name))
    elif ("you liv" in user):
         print("{}: mabolaje".format(name))
    elif ("crazy" in user):
         print("{}: mad".format(name))
    elif ("love" in user):
         print("{}: you are the cockroach in my cupboard".format(name))
    elif ("study" in user):
         print("{}: fine and yours?".format(name))
    elif ("old" in user):
         print("{}: 23".format(name))
    elif ("father name" in user):
         print("{}: ABDULRAFIU".format(name))
    elif ("level" in user):
         print("{}: ND 1".format(name))
    elif ("department" in user):
         print("{}: computer science tech".format(name))
    elif ("hello" in user):
         print("{}: how are you?".format(name))
    else:
       print("sorry {}, this is not in my dictionary".format(name))
    
     
     
     
    
