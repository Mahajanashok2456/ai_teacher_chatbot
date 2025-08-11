#!/usr/bin/env python3
"""
Setup script for AI Teacher Chatbot
Helps users install dependencies and configure the project.
"""

import os
import sys
import subprocess
import platform

def print_banner():
    """Print setup banner"""
    print("🎓 AI TEACHER CHATBOT - SETUP")
    print("=" * 40)

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    print("\n🔧 Setting up environment...")
    env_file = ".env"
    
    if os.path.exists(env_file):
        print("✅ .env file already exists")
        return True
    
    print("📝 Creating .env file...")
    env_content = """# Google Gemini API Configuration
# Get your API key from: https://makersuite.google.com/app/apikey
GOOGLE_API_KEY=your_google_api_key_here

# Optional: Customize the model (default: gemini-1.5-flash)
# GOOGLE_MODEL=gemini-1.5-flash

# Optional: Customize response length (default: 500)
# MAX_TOKENS=500

# Optional: Customize creativity level (default: 0.7)
# TEMPERATURE=0.7
"""
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ .env file created successfully!")
        print("⚠️  Please edit .env file and add your Google API key")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def test_installation():
    """Test if the installation works"""
    print("\n🧪 Testing installation...")
    try:
        import streamlit
        import google.generativeai
        import langdetect
        from dotenv import load_dotenv
        print("✅ All imports successful!")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def print_next_steps():
    """Print next steps for the user"""
    print("\n🎯 NEXT STEPS:")
    print("=" * 40)
    print("1. Edit the .env file and add your Google API key")
    print("2. Get your API key from: https://makersuite.google.com/app/apikey")
    print("3. Run the chatbot:")
    print("   • Web interface: streamlit run main.py")
    print("   • Demo: python demo.py")
    print("\n📚 For more information, see README.md")

def main():
    """Main setup function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Create .env file
    if not create_env_file():
        return
    
    # Test installation
    if not test_installation():
        return
    
    # Print next steps
    print_next_steps()
    
    print("\n🎉 Setup completed successfully!")

if __name__ == "__main__":
    main() 