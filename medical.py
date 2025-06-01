import sys

def greet():
    print("Hello! I'm your Medical Assistant Chatbot.")
    print("How can I help you today? (Type 'exit' to quit)")

def get_response(user_input):
    user_input = user_input.lower()
    if "fever" in user_input:
        return "If you have a fever, make sure to rest, stay hydrated, and monitor your temperature. If it persists or is very high, please consult a doctor."
    elif "headache" in user_input:
        return "For headaches, ensure you are hydrated and try to rest. If it's severe or persistent, consider seeking medical advice."
    elif "covid" in user_input or "corona" in user_input:
        return "Common COVID-19 symptoms include fever, cough, and difficulty breathing. If you suspect you have COVID-19, please get tested and follow local health guidelines."
    elif "cancer" in user_input:
        return "If you have a cancer I make sure, I'll give the best suggestions to find the tumour of your disease stage"
    elif "appointment" in user_input:
        return "To book an appointment, please contact your healthcare provider or use their online booking system."
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! Take care."
    else:
        return "I'm sorry, I can only provide general information. For specific health concerns, please consult a healthcare professional."

def main():
    greet()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Stay healthy.")
            sys.exit()
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()