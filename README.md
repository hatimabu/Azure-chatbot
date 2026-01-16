# AI Chatbot - Beginner Version

A simple chatbot that answers questions on various topics using OpenAI's API. Perfect for learning machine learning basics!

## 🎯 What This Project Does

- Takes questions on various topics
- Uses OpenAI (ChatGPT) to provide thoughtful answers
- Saves conversation history
- Runs on your local computer (no cloud needed yet!)

## 📁 Simple Folder Structure

```
ai-chatbot/
├── chatbot.py          # Main chatbot code (START HERE!)
├── config.py           # Settings and API keys
├── knowledge.py        # General knowledge base
├── requirements.txt    # Python packages needed
├── .env               # Your secret API key (create this)
├── .gitignore         # Files to ignore in git
├── conversations/     # Saved chats (auto-created)
└── README.md          # This file
```

## 🚀 Quick Start (5 Steps!)

### Step 1: Install Python
Make sure you have Python 3.8+ installed:
```bash
python --version
```

### Step 2: Get OpenAI API Key
1. Go to https://platform.openai.com/
2. Create an account (you'll get $5 free credit)
3. Go to API Keys section
4. Create a new key and copy it

### Step 3: Clone and Setup
```bash
# Create project folder
mkdir ai-chatbot
cd ai-chatbot

# Create virtual environment
python -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### Step 4: Add Your API Key
Create a file called `.env` and add:
```
OPENAI_API_KEY=your-key-here
```

### Step 5: Run It!
```bash
python chatbot.py
```

## 💬 How to Use

Once running, you'll see:
```
AI Chatbot Ready! Type 'quit' to exit.

You: What is machine learning?
Bot: Machine learning is a type of AI that...
```

## 🧠 Learning Path

### Week 1: Understanding the Basics
- Run the chatbot and see how it works
- Read through `chatbot.py` - it's heavily commented!
- Try asking different questions
- Look at saved conversations in `conversations/` folder

### Week 2: Customization
- Modify `knowledge.py` to add more general knowledge
- Change the chatbot's personality in `config.py`
- Experiment with different questions

### Week 3: Improvement
- Add question validation
- Implement better error handling
- Track which topics are asked most

### Month 2: Add Features
- Save conversations to a simple database
- Add a web interface (Flask)
- Deploy to cloud (Heroku free tier)

### Month 3+: Advanced
- Learn about RAG (Retrieval-Augmented Generation)
- Add vector databases
- Move to Azure (the complex version!)

## 📊 How It Works (Simple Explanation)

```
1. You ask a question
   ↓
2. Code sends it to OpenAI API
   ↓
3. OpenAI thinks and generates answer
   ↓
4. Code receives answer
   ↓
5. Shows you the answer
   ↓
6. Saves conversation to file
```

## 🎓 Key ML Concepts You'll Learn

1. **API Integration** - How to use AI services
2. **Prompt Engineering** - Crafting good questions for AI
3. **Context Management** - Keeping conversation history
4. **Data Storage** - Saving and loading conversations
5. **Error Handling** - Dealing with API failures

## 💰 Cost

- OpenAI gives $5 free credit (about 500-1000 questions!)
- After that: ~$0.002 per question (very cheap)
- This basic version costs almost nothing to learn with

## 🐛 Troubleshooting

**"Module not found"**
```bash
pip install -r requirements.txt
```

**"Invalid API key"**
- Check your `.env` file
- Make sure no extra spaces around the key

**"Rate limit exceeded"**
- You're making too many requests
- Wait a minute and try again

## 🔒 Important Notes

1. **Never share your API key** - Keep `.env` file private
2. **Don't commit `.env` to GitHub** - It's in `.gitignore`
3. **AI limitations** - This is a learning tool, answers may not always be perfectly accurate
4. **Always verify** - Check important information from reliable sources

## 📚 Next Steps After This

Once comfortable, you can:
1. Add a simple web interface
2. Deploy to cloud (Heroku/Railway)
3. Learn vector databases
4. Upgrade to the advanced version I created earlier

## 🤝 Getting Help

- Comment your code with questions
- Google error messages
- Ask in programming communities
- The code is simple on purpose - read it!

## 📖 Recommended Learning Resources

**Python Basics:**
- Python for Everybody (free course)
- Automate the Boring Stuff with Python

**Machine Learning:**
- Andrew Ng's ML course (Coursera)
- Fast.ai (practical approach)

**OpenAI API:**
- OpenAI Cookbook (official examples)
- OpenAI Documentation

## 🎯 Project Goals

✅ Learn ML basics
✅ Understand API integration  
✅ Build something useful
✅ Foundation for advanced projects
✅ Have fun!

---

**Remember:** This is a LEARNING project. Start simple, experiment, break things, fix them, and gradually improve. You'll be surprised how much you learn by just building and trying things!

Ready to code? Start with `chatbot.py` - it's heavily commented to teach you as you read!