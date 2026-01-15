#!/bin/bash

# Simple setup script for beginners
# Run this with: bash setup.sh

echo "🕌 Islamic Chatbot Setup"
echo "========================"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found!"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

echo "✅ Virtual environment created!"
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

echo "✅ Virtual environment activated!"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing required packages..."
pip install -r requirements.txt

echo "✅ All packages installed!"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your OpenAI API key!"
    echo ""
fi

# Create conversations folder
mkdir -p conversations

echo "========================"
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your OpenAI API key"
echo "2. Run: python chatbot.py"
echo ""
echo "Need help? Read README.md"
echo "========================"