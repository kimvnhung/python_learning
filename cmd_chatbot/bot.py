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
    "What is your favorite song?",
    "I like Bohemian Rhapsody.",
    "What is your favorite band?",
    "I like The Beatles.",
    "What is your favorite animal?",
    "I like cats.",
    "What is your favorite hobby?",
    "I like reading.",
    "What is your favorite sport?",
    "I like soccer.",
    "What is your favorite video game?",
    "I like Minecraft.",
    "What is your favorite TV show?",
    "I like Breaking Bad.",
    "What is your favorite actor?",
    "I like Tom Hanks.",
    "What is your favorite actress?",
    "I like Meryl Streep.",
    "What is your favorite director?",
    "I like Steven Spielberg.",
    "What is your favorite author?",
    "I like Stephen King.",
    "What is your favorite poet?",
    "I like Emily Dickinson.",
    "What is your favorite painter?",
    "I like Pablo Picasso.",
    "What is your favorite musician?",
    "I like Ludwig van Beethoven.",
])

#Add more training data here
trainer.train([
    "How can I help you?",
    "I need help with a problem.",
    "What is the problem?",
    "I am having trouble with my computer.",
    "What is the issue?",
    "My computer is running slow.",
    "Have you tried restarting your computer?",
    "Yes, I have.",
    "Have you tried running a virus scan?",
    "No, I have not.",
    "You should try that.",
    "Okay, I will.",
    "Let me know if you need any more help.",
    "Thank you.",
    "You're welcome.",
    "How can I help you?",
    "I need help with a problem.",
    "What is the problem?",
    "I am having trouble with my phone.",
    "What is the issue?",
    "My phone is not charging.",
    "Have you tried using a different charger?",
    "Yes, I have.",
    "Have you tried using a different outlet?",
    "No, I have not.",
    "You should try that.",
    "Okay, I will.",
    "Let me know if you need any more help.",
    "Thank you.",
    "You're welcome.",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")