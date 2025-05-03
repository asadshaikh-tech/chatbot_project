from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

faq = {
    "what is your name": "I am a simple chatbot.",
    "how are you": "I'm just code, but thanks for asking!",
    "what is flask": "Flask is a lightweight Python web framework.",
    "how does this chatbot work": "It matches your input with predefined responses.",
    "bye": "Goodbye! Have a great day!"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("message").lower()
    response = faq.get(user_input, "Sorry, I don't understand that.")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

