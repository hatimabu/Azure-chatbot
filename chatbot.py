"""
AI Chatbot - Main File
This is the heart of your chatbot. Read through the comments to understand each part!
"""

import os
import json
from datetime import datetime
from openai import OpenAI
from config import SYSTEM_PROMPT, CHATBOT_CONFIG
from knowledge import get_relevant_context

# Load API key from environment variable
# (We'll store this in a .env file)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class Chatbot:
    """
    Our chatbot class - this organizes all the chatbot functionality
    Think of it like a container that holds all the chatbot's abilities
    """
    
    def __init__(self):
        """
        Initialize the chatbot (this runs when we create a new chatbot)
        We set up an empty conversation history
        """
        self.conversation_history = []
        self.conversations_folder = "conversations"
        
        # Create folder to save conversations if it doesn't exist
        if not os.path.exists(self.conversations_folder):
            os.makedirs(self.conversations_folder)
    
    def add_message(self, role, content):
        """
        Add a message to our conversation history
        role = "user" or "assistant"
        content = the actual message text
        """
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def get_response(self, user_message):
        """
        This is the main function - it sends your question to OpenAI
        and gets back an answer
        """
        
        # Step 1: Add the user's message to history
        self.add_message("user", user_message)
        
        # Step 2: Get relevant knowledge for context
        # This helps the AI give better answers
        context = get_relevant_context(user_message)
        
        # Step 3: Build the messages to send to OpenAI
        # We include: system prompt + context + conversation history
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "system", "content": f"Context: {context}"}
        ] + self.conversation_history
        
        try:
            # Step 4: Call OpenAI API
            # This is where the magic happens!
            response = client.chat.completions.create(
                model=CHATBOT_CONFIG["model"],
                messages=messages,
                temperature=CHATBOT_CONFIG["temperature"],
                max_tokens=CHATBOT_CONFIG["max_tokens"]
            )
            
            # Step 5: Extract the assistant's reply
            assistant_message = response.choices[0].message.content
            
            # Step 6: Add assistant's response to history
            self.add_message("assistant", assistant_message)
            
            return assistant_message
            
        except Exception as e:
            # If something goes wrong, return an error message
            error_message = f"Sorry, I encountered an error: {str(e)}"
            return error_message
    
    def save_conversation(self):
        """
        Save the conversation to a JSON file
        This is useful for reviewing past conversations
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.conversations_folder}/conversation_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.conversation_history, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Conversation saved to {filename}")


def main():
    """
    Main function - this runs when you start the program
    It creates the chatbot and handles the conversation loop
    """
    
    print("=" * 60)
    print("🤖 AI Chatbot - Beginner Version")
    print("=" * 60)
    print("\nWelcome! I'm here to help answer your questions.")
    print("Type your question and press Enter.")
    print("Type 'quit' to exit and save the conversation.\n")
    
    # Create a new chatbot instance
    chatbot = Chatbot()
    
    # Main conversation loop
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check if user wants to quit
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\n👋 Goodbye! Have a great day!")
            chatbot.save_conversation()
            break
        
        # Skip empty messages
        if not user_input:
            continue
        
        # Get response from chatbot
        print("\n🤖 Bot: ", end="")
        response = chatbot.get_response(user_input)
        print(response)
        print()  # Empty line for readability


# This runs when you execute: python chatbot.py
if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY not found!")
        print("Please create a .env file with your API key.")
        print("See README.md for instructions.")
    else:
        main()