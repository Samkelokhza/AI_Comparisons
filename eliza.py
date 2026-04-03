from nltk.chat.eliza import eliza_chatbot

def get_eliza_response(user_input: str) -> str:
    return eliza_chatbot.respond(user_input)

if __name__ == "__main__":
    print("ELIZA Chatbot")
    print("Hello My name is David ,I feel stressed ,I am tired ,Because I have exams quit")
rules = {
    "I feel stressed": "Why do you think stress affects you?",
    "I am tired": "Have you been resting enough?",
    "My mother is strict": "Tell me more about your relationship with your mother.",
    "Because I have exams": "Exams can be tough. How are you preparing?",
    "I need more sleep": "Sleep is important. What keeps you awake?"
}
    eliza_chatbot.converse()