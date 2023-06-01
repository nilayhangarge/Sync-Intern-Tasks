import random

R_EATING = "I can't eat, I'm Chatbot!"
R_ADVICE = "I am not free here to give advice, ask google!"
R_MARRIED = "Yes I am Married With Alexa..!"


def unknown():
    response = ["Could you please Ask Again? ",
                "...",
                "Please Speak Again.",
                "What does that mean?"][
        random.randrange(4)]
    return response
