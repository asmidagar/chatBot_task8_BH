print("Hi! I’m ChatBot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("ChatBot: Hello! How can I help you?")
    elif user_input in ["how are you?", "how are you"]:
        print("ChatBot: I’m good, thank you! What about you?")
    elif user_input in ["i am fine", "i am good"]:
        print("ChatBot: That’s great to hear!")
    elif user_input in ["what is your name?", "who are you?"]:
        print("ChatBot: I’m a simple chatbot created with Python.")
    elif user_input in ["i want some help", "can you help me?"]:
        print("ChatBot: Yess please let me know, I would love to help")
    elif user_input in ["how were you build?", "what is your origin", "who created you"]:
        print("I was created by Asmi Dagar, intern at BroskiesHub")
    elif user_input in ['how do you perform?', "what are your functions"]:
        print("I am rule-based chatbot, built on the principle of if-elif-else")
    elif user_input in ["Why were you made?", "What were you made for"]:
        print("I was made under an python internship, to understand basis of NLP(non-AI)")
    elif user_input in ["bye", "exit", "quit"]:
        print("ChatBot: Goodbye! Have a great day!")
        break
    else:
        print("ChatBot: Sorry, I didn’t understand that.")