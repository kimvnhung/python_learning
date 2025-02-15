# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Hello",
    "How are you?",
    "I'm doing great.",
    "That is good to hear.",
    "Thank you.",
    "You're welcome.",
    "What is your name?",
    "My name is Chatbot.",
    "What is your favorite color?",
    "I like blue.",
    "What is your favorite food?",
    "I like pizza.",
    "What is your favorite movie?",
    "I like The Matrix.",
    "What is your favorite book?",
    "I like The Great Gatsby.",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")