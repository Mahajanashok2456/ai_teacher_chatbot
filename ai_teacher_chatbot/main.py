import streamlit as st
import google.generativeai as genai
import os
from langdetect import detect
import json

# Configure Google Gemini API
# API key will be set by user input

# Initialize translator (removed googletrans dependency)
# translator = Translator()

# Teacher prompts for different languages
TEACHER_PROMPTS = {
    'en': """You are a knowledgeable and patient teacher. Provide clear, educational responses that include:
    - Clear definitions and explanations
    - Relevant examples
    - Step-by-step breakdowns when appropriate
    - Encouraging and supportive tone
    Always respond in English.""",
    
    'hi': """आप एक जानकार और धैर्यवान शिक्षक हैं। स्पष्ट, शैक्षिक प्रतिक्रियाएं दें जिनमें शामिल हों:
    - स्पष्ट परिभाषाएं और स्पष्टीकरण
    - प्रासंगिक उदाहरण
    - जहां उचित हो वहां चरण-दर-चरण विवरण
    - प्रोत्साहन और सहायक स्वर
    हमेशा हिंदी में जवाब दें।""",
    
    'te': """మీరు ఒక జ్ఞానవంతుడు మరియు ఓపికగల ఉపాధ్యాయుడు. స్పష్టమైన, విద్యాసంబంధమైన సమాధానాలను అందించండి:
    - స్పష్టమైన నిర్వచనాలు మరియు వివరణలు
    - సంబంధిత ఉదాహరణలు
    - సరైన సమయంలో దశలవారీ వివరణలు
    - ప్రోత్సాహకరమైన మరియు సహాయకరమైన ధోరణి
    ఎల్లప్పుడూ తెలుగులో సమాధానం ఇవ్వండి."""
}

def detect_language(text):
    """Detect the language of input text"""
    try:
        lang = detect(text)
        return lang
    except:
        return 'en'  # Default to English

def translate_text(text, target_lang):
    """Translate text to target language (simplified version)"""
    # For now, return the original text since we removed googletrans
    return text

def get_teacher_response(user_input, language, api_key):
    """Get response from Google Gemini API with teacher persona"""
    if not api_key:
        return "⚠️ Please enter your Google API key in the sidebar to start chatting!"
    
    try:
        # Configure API with user's key
        genai.configure(api_key=api_key)
        
        # Get the appropriate teacher prompt
        teacher_prompt = TEACHER_PROMPTS.get(language, TEACHER_PROMPTS['en'])
        
        # Create the full prompt
        full_prompt = f"{teacher_prompt}\n\nUser question: {user_input}"
        
        # Try different model names
        model_names = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
        
        for model_name in model_names:
            try:
                # Create Gemini model
                model = genai.GenerativeModel(model_name)
                
                # Generate response
                response = model.generate_content(full_prompt)
                
                return response.text
            except Exception as model_error:
                continue
        
        return f"Sorry, I couldn't find a working Gemini model. Please check your API key and try again."
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

def main():
    st.set_page_config(
        page_title="AI Teacher Chatbot",
        page_icon="🎓",
        layout="wide"
    )
    
    st.title("🎓 AI Teacher Chatbot")
    st.markdown("### Your Personal AI Teacher - Supporting English, Hindi, and Telugu")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("Settings")
        
        # API Key input
        api_key = st.text_input("Enter your Google API Key:", type="password", help="Get your API key from https://makersuite.google.com/app/apikey")
        if api_key:
            st.success("✅ API Key entered successfully!")
        else:
            st.warning("⚠️ Please enter your Google API key to start chatting!")
        
        language_choice = st.selectbox(
            "Choose Interface Language:",
            ["English", "हिंदी", "తెలుగు"],
            index=0
        )
        
        # Map language choice to language code
        lang_map = {"English": "en", "हिंदీ": "hi", "తెలుగు": "te"}
        interface_lang = lang_map[language_choice]
        
        st.markdown("---")
        st.markdown("### How to use:")
        st.markdown("1. Type your question in any language")
        st.markdown("2. The AI will detect the language and respond accordingly")
        st.markdown("3. You can ask about any educational topic")
        st.markdown("4. Get clear explanations and examples")
        
        st.markdown("---")
        st.markdown("**Supported Languages:**")
        st.markdown("- English 🇺🇸")
        st.markdown("- Hindi 🇮🇳")
        st.markdown("- Telugu 🇮🇳")
    
    # Main chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Detect language of user input
        detected_lang = detect_language(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_teacher_response(prompt, detected_lang, api_key)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Example questions
    st.markdown("---")
    st.markdown("### Example Questions You Can Ask:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**English:**")
        st.markdown("- What is photosynthesis?")
        st.markdown("- Explain quantum physics")
        st.markdown("- How does democracy work?")
    
    with col2:
        st.markdown("**हिंदी:**")
        st.markdown("- प्रकाश संश्लेषण क्या है?")
        st.markdown("- क्वांटम भौतिकी समझाएं")
        st.markdown("- लोकतंत्र कैसे काम करता है?")
    
    with col3:
        st.markdown("**తెలుగు:**")
        st.markdown("- కిరణజన్య సంయోగక్రియ అంటే ఏమిటి?")
        st.markdown("- క్వాంటం భౌతిక శాస్త్రాన్ని వివరించండి")
        st.markdown("- ప్రజాస్వామ్యం ఎలా పని చేస్తుంది?")

if __name__ == "__main__":
    main() 