from flask import Flask, render_template, request
from chatbot import EmpathicChatBot

chat_messages = []

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        chat_messages.append(f"Me: {user_input}")

        chatbot = EmpathicChatBot()
        
        response = chatbot.get_response(user_input)
        chat_messages.append(f"{chatbot.name}: {response}")

    return render_template("index.html", chat_messages=chat_messages)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8070, debug=True)
