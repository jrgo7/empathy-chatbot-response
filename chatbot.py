from chatterbot import ChatBot as cb

class EmpathicChatBot:
    def __init__(self):
        self.name = "John Adams"
        self.chatbot = cb(self.name)

    def get_response(self, message: str):
        if(message.lower() == "clear mem"):
            self.chatbot.storage.drop()
            return "Storage Cleared."
        
        response = self.chatbot.get_response(message)
        return response        