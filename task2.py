import nltk
from nltk.chat.util import Chat, reflections

# Ensure that necessary NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('wordnet')

# Pairs of patterns and responses for the chatbot
pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello! How can I help you today?", "Hey there! What can I do for you?"]
    ],
    [
        r"(what is your name|who are you)",
        ["I am a chatbot built with NLTK!", "You can call me Chatbot."]
    ],
    [
        r"how are you",
        ["I'm just a bot, but I'm doing great! How can I assist you?", "Feeling chatty today, how about you?"]
    ],
    [
        r"(what can you do|your features)",
        ["I can answer basic questions and engage in simple conversations!", "Try asking me something interesting."]
    ],
    [
        r"(bye|exit|quit)",
        ["Goodbye! Have a great day!", "See you next time!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you rephrase?", "I'm learning every day! Could you clarify?"]
    ]
]

# Creating the chatbot
chatbot = Chat(pairs, reflections)

# Function to start the chatbot interaction
def chatbot_main():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye! Take care.")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot_main()
