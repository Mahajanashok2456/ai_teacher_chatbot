#!/usr/bin/env python3
"""
Demo script for AI Teacher Chatbot
This script demonstrates the chatbot's capabilities with example conversations.
"""

import os
from dotenv import load_dotenv
from main import detect_language, get_teacher_response

# Load environment variables
load_dotenv()

def run_demo():
    """Run a demonstration of the AI Teacher Chatbot"""
    
    print("🎓 AI TEACHER CHATBOT - DEMO")
    print("=" * 50)
    
    # Check if Google API key is available
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Demo cannot run without Google API key!")
        print("Please set your GOOGLE_API_KEY in the .env file")
        return
    
    # Example conversations in different languages
    demo_conversations = [
        {
            "language": "English",
            "questions": [
                "What is photosynthesis?",
                "Explain the water cycle",
                "How does democracy work?"
            ]
        },
        {
            "language": "Hindi",
            "questions": [
                "प्रकाश संश्लेषण क्या है?",
                "जल चक्र क्या है?",
                "लोकतंत्र कैसे काम करता है?"
            ]
        },
        {
            "language": "Telugu",
            "questions": [
                "కిరణజన్య సంయోగక్రియ అంటే ఏమిటి?",
                "నీటి చక్రం అంటే ఏమిటి?",
                "ప్రజాస్వామ్యం ఎలా పని చేస్తుంది?"
            ]
        }
    ]
    
    for conversation in demo_conversations:
        print(f"\n🌍 {conversation['language']} Conversation:")
        print("-" * 40)
        
        for i, question in enumerate(conversation['questions'], 1):
            print(f"\nQ{i}: {question}")
            
            # Detect language
            detected_lang = detect_language(question)
            print(f"   Detected language: {detected_lang}")
            
            # Get AI response
            print("   AI Teacher is thinking...")
            try:
                response = get_teacher_response(question, detected_lang)
                print(f"   A{i}: {response[:200]}...")  # Show first 200 characters
            except Exception as e:
                print(f"   Error: {str(e)}")
            
            print()
    
    print("=" * 50)
    print("🎯 Demo completed!")
    print("\nTo run the full chatbot:")
    print("  • Web interface: streamlit run main.py")

if __name__ == "__main__":
    run_demo() 