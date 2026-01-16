"""
Azure Function version of the chatbot
This is what runs in the cloud when deployed

NOTE: This will be created when you're ready to deploy
For now, you use the local chatbot.py
"""

import logging
import json
import os
import azure.functions as func
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Create function app
app = func.FunctionApp()

@app.function_name(name="chat")
@app.route(route="chat", methods=["POST"])
def chat_function(req: func.HttpRequest) -> func.HttpResponse:
    """
    Main chatbot endpoint for Azure
    
    POST /api/chat
    Body: {
        "message": "What are the five pillars?",
        "conversation_id": "optional"
    }
    """
    logging.info('Processing chat request')
    
    try:
        # Parse request
        req_body = req.get_json()
        
        if 'message' not in req_body:
            return func.HttpResponse(
                json.dumps({"error": "Message field required"}),
                status_code=400,
                mimetype="application/json"
            )
        
        user_message = req_body.get('message')
        conversation_id = req_body.get('conversation_id', 'default')
        
        # System prompt
        system_prompt = """You are a knowledgeable Islamic chatbot assistant.
        Provide accurate, respectful answers about Islam.
        Cite sources when possible and maintain Islamic etiquette."""
        
        # Call OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        assistant_message = response.choices[0].message.content
        
        # TODO: Save to Cosmos DB when integrated
        
        # Return response
        result = {
            "response": assistant_message,
            "conversation_id": conversation_id,
            "model": "gpt-3.5-turbo",
            "status": "success"
        }
        
        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json"
        )
        
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )


@app.function_name(name="health")
@app.route(route="health", methods=["GET"])
def health_check(req: func.HttpRequest) -> func.HttpResponse:
    """
    Health check endpoint
    GET /api/health
    """
    return func.HttpResponse(
        json.dumps({"status": "healthy", "service": "ai-chatbot"}),
        status_code=200,
        mimetype="application/json"
    )