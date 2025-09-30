from chatterbot import ChatBot as cb
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from conversations import sample_conversations

class EmpathicChatBot():
    def __init__(self):
        self.name = "Emio"
        self.chatbot = cb(self.name)
        trainer = ListTrainer(self.chatbot)
        for conversation in sample_conversations:
            trainer.train(conversation)
            
        trainer2 = ChatterBotCorpusTrainer(self.chatbot)
        trainer2.train("greetings")

    def get_response(self, message: str):
        if message.lower() == "clear mem":
            self.chatbot.storage.drop()
            return "Storage Cleared."

        response = self.chatbot.get_response(message)
        return response
