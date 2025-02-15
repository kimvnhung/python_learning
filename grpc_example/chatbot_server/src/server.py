# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import chatbot_pb2
import chatbot_pb2_grpc
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



# class Greeter(helloworld_pb2_grpc.GreeterServicer):
#     def SayHello(self, request, context):
#         return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

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

class Chatboter(chatbot_pb2_grpc.ChatboterServicer):
    def CheckHealth(self, request, context):
        return chatbot_pb2.HealthCheckResponse(message="I'm alive! %s!" % request.name)
    
    def TrainModel(self, request, context):
        return chatbot_pb2.TrainModelResponse(message="Placeholder for training model", status=200)

    def GetResponse(self, request, context):
        if not request.message:
            return chatbot_pb2.GetResponseResponse(message="No message provided", status=400)
        temp = chatbot.get_response(request.message)
        if not temp:
            return chatbot_pb2.GetResponseResponse(message="No response found", status=404)
        
        return chatbot_pb2.GetResponseResponse(message=str(temp), status=200)

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatbot_pb2_grpc.add_ChatboterServicer_to_server(Chatboter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()