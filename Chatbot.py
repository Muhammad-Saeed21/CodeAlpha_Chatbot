# Project       : Simple Chatbot
# Author        : Muhammad Saeed
# Internship    : CodeAlpha - Python Programming Internship
# Description   : A simple rule-based chatbot that responds to greetings, questions, 
#                 gratitude, and farewells using keyword matching.

# Function to get chatbot response based on user input
def chatbot_response(user_input):
    # Convert user input to lowercase to make comparisons case-insensitive
    user_input = user_input.lower()

    # Lists of keywords for different categories
    greetings = ["hello", "hi", "hey"]  # Words that indicate a greeting
    farewells = ["bye", "goodbye", "see you"]  # Words that indicate saying goodbye
    thanks = ["thank you", "thanks"]  # Words that indicate gratitude

    # Check if the user input contains any greeting word
    if any(word in user_input for word in greetings):
        return " Hi there! How can I help you ? "  # Fixed greeting response
    
    # Check if the user asks "how are you"
    elif "how are you" in user_input:
        return " I'm just a program, but I'm great! "  # Fixed response
    
    # Check if the user asks for the chatbot's name
    elif "your name" in user_input:
        return " I'm a simple chatbot created by Muhammad Saeed! "
    
    # Check if the user asks for help
    elif "help" in user_input:
        return " Sure! You can ask me greetings, my name, how I am, or say goodbye! "
    
    # Check if the user asks what the chatbot can do
    elif "what can you do" in user_input:
        return " I can chat with you and answer simple questions. I'm still learning! "
    
    # Check if the user says thanks
    elif any(word in user_input for word in thanks):
        return " You're welcome! "  # Fixed response
    
    # Check if the user says goodbye
    elif any(word in user_input for word in farewells):
        return " Goodbye! Have a great day! "  # Fixed response
    
    # Default response when input is not understood
    else:
        return " Sorry, I didn't understand that. Can you try saying it differently ? "


# ----------------------------
# Console-based interface
# ----------------------------
print(" Chatbot is online! Type 'bye' to exit. ")  # Welcome message

while True:
    user_input = input(" You : ")  # Take input from user
    response = chatbot_response(user_input)  # Get chatbot response
    print(" Bot : ", response)  # Print chatbot response
    
    # Exit the chatbot if the user says goodbye
    if any(word in user_input.lower() for word in ["bye", "goodbye", "see you"]):
        break  # Exit the loop
