import streamlit as st

def get_response(user_input):
    user_input = user_input.lower()
    if "fever" in user_input:
        return "If you have a fever, make sure to rest, stay hydrated, and monitor your temperature. If it persists or is very high, please consult a doctor."
    elif "headache" in user_input:
        return "For headaches, ensure you are hydrated and try to rest. If it's severe or persistent, consider seeking medical advice."
    elif "covid" in user_input or "corona" in user_input:
        return "Common COVID-19 symptoms include fever, cough, and difficulty breathing. If you suspect you have COVID-19, please get tested and follow local health guidelines."
    elif "cancer" in user_input:
        return "If you have a cancer I make sure, I'll help to find the tumour of your disease stage"
    elif "appointment" in user_input:
        return "To book an appointment, please contact your healthcare provider or use their online booking system."
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! Take care."
    else:
        return "I'm sorry, I can only provide general information. For specific health concerns, please consult a healthcare professional."

st.title("Medical Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")

if st.button("Send") or user_input:
    if user_input:
        bot_response = get_response(user_input)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", bot_response))
        user_input = ""

for speaker, text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"<div style='text-align: right; color: blue;'><b>You:</b> {text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: red; color: green;'><b>Bot:</b> {text}</div>", unsafe_allow_html=True)