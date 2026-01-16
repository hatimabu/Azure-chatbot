"""
Configuration file - All settings in one place
You can easily modify the chatbot's behavior here
"""

# System Prompt - This tells the AI how to behave
# Think of it as giving instructions to a helper
SYSTEM_PROMPT = """You are a helpful and knowledgeable AI assistant.

Your purpose:
- Answer questions on a wide variety of topics
- Provide accurate and helpful information
- Be patient and understanding with all questions
- Use simple, clear language that anyone can understand

Guidelines:
1. Always be respectful and helpful to users
2. Provide accurate information to the best of your ability
3. If you're unsure about something, admit it honestly
4. Be concise but thorough in your answers
5. Draw from general knowledge across various domains

Remember: You're here to assist and inform users on any topic they ask about.
"""

# Chatbot Configuration
# These settings control how the AI responds
CHATBOT_CONFIG = {
    # Model to use - gpt-3.5-turbo is cheaper and faster for learning
    # gpt-4 is more accurate but costs more
    "model": "gpt-3.5-turbo",
    
    # Temperature controls creativity (0.0 = focused, 1.0 = creative)
    # For religious questions, we want focused answers
    "temperature": 0.7,
    
    # Maximum tokens (words) in response
    # Lower = shorter answers, saves money
    "max_tokens": 500,
}

# You can add more configurations here as you learn!
# Examples:
# - Different system prompts for different topics
# - Language preferences
# - Response length preferences