# you can change the command as per file_name to run the FastAPI app
from openai import OpenAI
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from typing import Annotated

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = FastAPI()

chat_log = []

# # Define a GET route for root
# @app.get("/")
# async def root():
#     return {"message": "Welcome to the chat API. Use POST requests to interact with /."}


@app.post("/")
async def chat(user_input: Annotated[str, Form()]):

    chat_log.append({'role': 'user', 'content': user_input})
    
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=chat_log,
    temperature=0.5, 
    max_tokens = 50
    )

    bot_response = response.choices[0].message.content
    chat_log.append({'role':'assistant', 'content':bot_response})
    
    return bot_response


# Run the file : uvicorn main:app --reload (uvicorn fastapi_chatbot:app --reload) or > python -m uvicorn main:app --reload
# http://127.0.0.1:8000/docs
