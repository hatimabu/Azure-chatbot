"""
Knowledge Base - General information for context
This is a simple version - later you'll learn to use databases!
"""

# Basic general knowledge - we'll search through this for relevant info
GENERAL_KNOWLEDGE = {
    "programming": """
    Programming Basics:
    - Programming is writing instructions for computers
    - Common languages: Python, JavaScript, Java, C++
    - Key concepts: variables, loops, functions, classes
    - Problem-solving and logical thinking are essential
    - Practice regularly to improve skills
    """,

    "ai_ml": """
    Artificial Intelligence and Machine Learning:
    - AI: Machines performing tasks that typically require human intelligence
    - Machine Learning: AI systems that learn from data
    - Applications: Chatbots, image recognition, recommendations
    - Requires large amounts of quality data for training
    - Ethics and responsible use are important considerations
    """,

    "health": """
    Health and Wellness:
    - Balanced diet with fruits, vegetables, and lean proteins
    - Regular exercise: 150 minutes of moderate activity weekly
    - Adequate sleep: 7-9 hours per night for adults
    - Mental health is as important as physical health
    - Regular check-ups and preventive care save lives
    """,

    "environment": """
    Environmental Protection:
    - Climate change is caused by human activities
    - Reduce carbon footprint through sustainable choices
    - Conservation: Reduce, reuse, recycle
    - Renewable energy sources: Solar, wind, hydro
    - Protect biodiversity and natural habitats
    """,

    "education": """
    Education and Learning:
    - Lifelong learning keeps the mind active
    - Different learning styles: visual, auditory, kinesthetic
    - Setting goals and maintaining discipline helps success
    - Technology enhances but doesn't replace traditional learning
    - Critical thinking and problem-solving are key skills
    """,

    "technology": """
    Technology Trends:
    - Cloud computing enables scalable applications
    - Internet of Things connects everyday devices
    - Cybersecurity protects digital information
    - Blockchain provides secure, transparent transactions
    - Quantum computing may revolutionize computing power
    """,
}

# Simple keywords to help find relevant knowledge
KEYWORDS = {
    "programming": ["programming", "code", "coding", "developer", "python", "javascript"],
    "ai_ml": ["ai", "artificial intelligence", "machine learning", "ml", "chatbot", "neural"],
    "health": ["health", "wellness", "exercise", "diet", "sleep", "medical"],
    "environment": ["environment", "climate", "sustainability", "green", "eco", "nature"],
    "education": ["education", "learning", "study", "school", "knowledge", "teach"],
    "technology": ["technology", "tech", "computer", "software", "hardware", "digital"],
}


def get_relevant_context(user_message):
    """
    Simple function to find relevant knowledge based on user's question
    
    This is a BASIC version. Later you'll learn about:
    - Vector databases
    - Semantic search
    - RAG (Retrieval-Augmented Generation)
    
    For now, we just check if keywords appear in the question
    """
    
    # Convert message to lowercase for easier matching
    message_lower = user_message.lower()
    
    # List to store relevant knowledge
    relevant_info = []
    
    # Check each topic
    for topic, keywords in KEYWORDS.items():
        # If any keyword is in the message
        if any(keyword in message_lower for keyword in keywords):
            # Add that topic's knowledge
            relevant_info.append(GENERAL_KNOWLEDGE[topic])
    
    # If we found relevant info, return it
    if relevant_info:
        return "\n\n".join(relevant_info)
    
    # Otherwise, return a general statement
    return "General knowledge and information on various topics."


# You can add more knowledge here as you learn!
# Later, you'll move this to:
# - Text files
# - JSON files
# - Databases
# - Vector databases (advanced!)

def add_knowledge(topic, content):
    """
    Function to add new knowledge (for future expansion)
    Right now, you'd just edit ISLAMIC_KNOWLEDGE directly
    """
    GENERAL_KNOWLEDGE[topic] = content
    print(f"Added knowledge about: {topic}")


# Example of how you might expand this later:
# - Load from external files
# - Connect to a database
# - Use embeddings for better matching
# - Add source citations