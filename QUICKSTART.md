# 🚀 Quick Start Guide (5 Minutes!)

Follow these steps to get your chatbot running TODAY.

## Step 1: Get an OpenAI API Key (2 minutes)

1. Go to https://platform.openai.com/
2. Click "Sign Up" (or "Log In" if you have an account)
3. Once logged in, click your profile → "View API Keys"
4. Click "Create new secret key"
5. **COPY THE KEY** (you won't see it again!)
6. You get $5 free credit = ~500-1000 questions!

## Step 2: Setup Your Project (2 minutes)

### On Mac/Linux:
```bash
# Create folder
mkdir ai-chatbot
cd ai-chatbot

# Run setup
bash setup.sh

# Add your API key to .env file
nano .env
# (paste your key, then press Ctrl+X, Y, Enter to save)
```

### On Windows:
```bash
# Create folder
mkdir ai-chatbot
cd ai-chatbot

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Create .env file
copy .env.example .env
# Then open .env with Notepad and add your key
```

## Step 3: Run It! (1 minute)

```bash
python chatbot.py
```

You should see:
```
🤖 AI Chatbot - Beginner Version
========================================

Welcome! I'm here to help answer your questions.
Type your question and press Enter.
Type 'quit' to exit and save the conversation.

You:
```

## First Question to Try

```
You: What is machine learning?
```

The bot will explain it to you!

## Common Issues

**"ModuleNotFoundError: No module named 'openai'"**
```bash
pip install -r requirements.txt
```

**"Error: OPENAI_API_KEY not found!"**
- Make sure you created the `.env` file
- Make sure you pasted your API key correctly
- Check there are no extra spaces

**"RateLimitError"**
- You're asking too fast
- Wait 1 minute and try again
- Or your free credit ran out ($5)

## What to Do Next

1. **Play with it** - Ask 5-10 different questions
2. **Look at the code** - Open `chatbot.py` and read the comments
3. **Check saved conversations** - Look in the `conversations/` folder
4. **Modify it** - Try changing the system prompt in `config.py`

## Learning Path

**Day 1:** Get it running and ask questions
**Day 2:** Read and understand `chatbot.py`
**Day 3:** Read and understand `config.py` and `knowledge.py`
**Day 4:** Try modifying the system prompt
**Day 5:** Add new general knowledge to `knowledge.py`

**Week 2:** Start learning about:
- How the OpenAI API works
- What "temperature" and "tokens" mean
- How to improve responses

**Week 3:** Add features:
- Web interface with Flask
- Better knowledge base
- User preferences

## Need Help?

1. Read the error message carefully
2. Google the exact error
3. Check OpenAI documentation
4. Ask in coding communities

## Remember

- This is a LEARNING project
- It's okay if you don't understand everything
- Break things and fix them - that's how you learn!
- Start simple, add complexity gradually

**Happy coding! 🚀**