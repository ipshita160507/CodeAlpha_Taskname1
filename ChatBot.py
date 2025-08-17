def chatbot():
    print("Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")
    enter=["hello","how are you","what is the weather","bye"]
    for enter2 in enter:

        enter2= input("Please chat here:")
        if enter2== "hello":
            print("Chatbot: Hi there!")
        elif enter2 == "how are you":
            print("Chatbot: I'm fine, thanks! How about you?")
        elif enter2 =="what is the weather":
            print("Chatbot: It is a sunny weather")   
        elif enter2 == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I didn't get that.")

# Run the chatbot
chatbot()