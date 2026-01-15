"""
Knowledge Base - Islamic information for context
This is a simple version - later you'll learn to use databases!
"""

# Basic Islamic knowledge - we'll search through this for relevant info
ISLAMIC_KNOWLEDGE = {
    "five_pillars": """
    The Five Pillars of Islam:
    1. Shahada - Declaration of faith: "There is no god but Allah, and Muhammad is His messenger"
    2. Salah - Five daily prayers
    3. Zakat - Giving charity (2.5% of wealth annually)
    4. Sawm - Fasting during Ramadan
    5. Hajj - Pilgrimage to Mecca once in a lifetime if able
    """,
    
    "prayer": """
    Prayer (Salah) in Islam:
    - Muslims pray 5 times daily: Fajr (dawn), Dhuhr (noon), Asr (afternoon), Maghrib (sunset), Isha (night)
    - Prayer involves physical movements and recitation
    - Direction: Facing the Kaaba in Mecca (Qibla)
    - Purpose: Direct connection with Allah
    - Can be performed individually or in congregation
    """,
    
    "ramadan": """
    Ramadan:
    - The 9th month of Islamic lunar calendar
    - Muslims fast from dawn to sunset
    - Fasting includes no food, drink, or intimate relations during daylight
    - Exceptions: Children, elderly, sick, pregnant, traveling
    - Purpose: Spiritual reflection, self-discipline, empathy for the poor
    - Ends with Eid al-Fitr celebration
    """,
    
    "quran": """
    The Quran:
    - Holy book of Islam, revealed to Prophet Muhammad (peace be upon him)
    - Written in Arabic, divided into 114 chapters (Surahs)
    - Considered the literal word of God (Allah)
    - Core teachings: Monotheism, morality, guidance for life
    - Muslims recite it in prayers and study its meanings
    """,
    
    "prophet": """
    Prophet Muhammad (peace be upon him):
    - Born in Mecca around 570 CE
    - Received first revelation at age 40
    - Final prophet in Islam
    - Teachings recorded in Hadith (sayings and actions)
    - Example of perfect character and conduct
    - Passed away in 632 CE in Medina
    """,
    
    "charity": """
    Charity in Islam (Zakat):
    - Mandatory: 2.5% of wealth annually (Zakat)
    - Voluntary: Sadaqah (any amount, any time)
    - Given to: Poor, needy, orphans, widows, etc.
    - Purpose: Purify wealth, help society, reduce inequality
    - One of the Five Pillars of Islam
    """,
}

# Simple keywords to help find relevant knowledge
KEYWORDS = {
    "five_pillars": ["pillar", "pillars", "foundation", "basic"],
    "prayer": ["prayer", "pray", "salah", "namaz"],
    "ramadan": ["ramadan", "fast", "fasting", "sawm"],
    "quran": ["quran", "koran", "book", "revelation", "scripture"],
    "prophet": ["prophet", "muhammad", "messenger"],
    "charity": ["charity", "zakat", "sadaqah", "giving", "poor"],
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
            relevant_info.append(ISLAMIC_KNOWLEDGE[topic])
    
    # If we found relevant info, return it
    if relevant_info:
        return "\n\n".join(relevant_info)
    
    # Otherwise, return a general statement
    return "General Islamic knowledge from authentic sources."


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
    ISLAMIC_KNOWLEDGE[topic] = content
    print(f"Added knowledge about: {topic}")


# Example of how you might expand this later:
# - Load from external files
# - Connect to a database
# - Use embeddings for better matching
# - Add source citations