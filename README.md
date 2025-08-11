# AI Teacher Chatbot

A multilingual AI-powered chatbot that acts as a knowledgeable teacher, supporting English, Hindi, and Telugu.

---

## 🚀 Setup Instructions

### 1. **Clone or Download the Repository**
```bash
git clone <repo-url>
cd ai_teacher_chatbot
```

### 2. **Create and Activate a Virtual Environment (Recommended)**
```bash
python -m venv venv
# For Windows PowerShell:
.\venv\Scripts\Activate.ps1
# For Windows Command Prompt:
venv\Scripts\activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Get Your Google Gemini API Key**
- Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- Copy your API key

### 5. **Configure API Key**
- Create a `.env` file in the project folder with this line:
  ```
  GOOGLE_API_KEY=your_api_key_here
  ```
  *or*  
- Enter your API key in the Streamlit sidebar when prompted.

---

## 🖥️ Running the Chatbot

### **Web Interface**
```bash
python -m streamlit run main.py
```
- Open the browser link shown in the terminal.
- Enter your API key if prompted.
- Start chatting in English, Hindi, or Telugu!

### **Demo Script (Command Line)**
```bash
python demo.py
```

---

## 🛠️ Troubleshooting

- If `streamlit` is not recognized, use `python -m streamlit run main.py`.
- Make sure your virtual environment is activated before installing or running.
- If you see missing package errors, re-run `pip install -r requirements.txt`.

---
