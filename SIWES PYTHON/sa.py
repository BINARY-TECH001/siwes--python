bot_dict = {
    "how are you" : "i am fine :), how are you too?",
    "weather" : "it is raining :( please try to stay indoor",
    "what name" : "my name is ADEMOLA, May i know your name too?",
    "go to school" : "Yes, i do go to school",
    "at home" : "Nope :( i am not home"
    }
print ("welcome to my ChatBot!\nPress (q) to quit")
print("Bot: Hello friend! ")

while True:
    u_input = input("You: ").lower()
    
    if u_input == "q":
        break
    
    for i in bot_dict:
        if i in u_input:
            print(f"Bot: {bot_dict[i]}")
        else:
           continue
print("Bot: sorry :( I have no reply for this")            

