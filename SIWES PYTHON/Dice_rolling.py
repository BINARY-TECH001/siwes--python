import random
mylist = [1,2,3,4,5,6]
newNumber = ""
for i in range(6) :
    randWord = random.choice(mylist)
    
    print(randWord)
