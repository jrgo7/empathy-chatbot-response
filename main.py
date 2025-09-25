from flask import Flask, render_template, request

chat_messages = []

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        chat_messages.append(user_input)
        """
        Do stuff with `user_input` e.g. generate a response.
        """
        response = "AI: Womp womp"
        chat_messages.append(response)

    return render_template("index.html", chat_messages=chat_messages)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
