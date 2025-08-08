📚 AI Teacher Chatbot
AI Teacher Chatbot is a multilingual, interactive chatbot designed to help students learn and get answers to their questions in English, Hindi, and Telugu. It uses the Google Gemini API to generate educational responses and features automatic language detection for a seamless user experience.

✨ Key Features
Multilingual Support – English, Hindi, and Telugu (auto-detected)

Educational Responses – Answers questions like a knowledgeable teacher

Web Interface – Built with Streamlit for easy interaction

Easy Setup – Quick start with a virtual environment and requirements file

Demo Script – Try out the chatbot from the command line

⚙️ How It Works
User asks a question in any supported language.

The chatbot detects the language automatically.

It generates a helpful, structured response using the Google Gemini API.

Users can interact via:

Web Interface (Streamlit)

Command-line Demo

🛠 Tech Stack
Python

Streamlit

Google Gemini API

langdetect

🚀 Getting Started
bash
Copy
Edit
# 1️⃣ Clone the repository
git clone https://github.com/your-username/ai-teacher-chatbot.git
cd ai-teacher-chatbot

# 2️⃣ Set up a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Add your Google Gemini API key
export GEMINI_API_KEY="your_api_key_here"

# 5️⃣ Run the chatbot (Streamlit Web App)
streamlit run app.py

# 6️⃣ OR run the command-line demo
python demo.py
