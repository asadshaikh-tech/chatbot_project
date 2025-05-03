# chatbot_project
# 💬 Simple Chatbot using Python & Flask

This is a beginner-level chatbot project built using Python and Flask as part of my internship. The chatbot can answer predefined FAQs and provide fallback responses for unknown inputs.

## 🚀 Features

- Responds to user-input questions
- Matches user input to a dictionary of FAQs
- Provides a default response when input is not understood
- Simple web interface using HTML and Flask

## 🛠️ Tech Stack

- Python 3.x
- Flask
- HTML

## 📂 Project Structure


## 💡 How It Works

- A dictionary maps common questions to specific answers.
- Flask handles routing and server logic.
- Jinja2 renders the web interface.
- When a user submits a question, the chatbot matches it to known ones or gives a default reply.

## ▶️ Getting Started

### 1. Clone the repository (or download manually)

git clone https://github.com/yourusername/chatbot_project.git

cd chatbot_project

2. Create and activate a virtual environment
   
python -m venv .venv

.venv\Scripts\activate

4. Install dependencies
pip install flask

5. Run the Flask app
python chatbot.py

6. Open in browser
Navigate to: http://127.0.0.1:5000
