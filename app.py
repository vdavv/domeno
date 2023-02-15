from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    message = data["message"]
    response = generate_response(message)
    return jsonify({"message": response})


def generate_response(message):
    greetings = ["hi", "hello", "hey"]
    if message.lower() in greetings:
        return "Hello, I'm a trademark registration assistant Domeno!"
    else:
        return "I'm sorry, I don't understand what you're saying."


if __name__ == "__main__":
    app.run(debug=True)
