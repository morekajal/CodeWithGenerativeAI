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

chat_log = [{'role' : 'system',
             'content' : 'You are a Python tutor AI, completely dedicated to teach users how to learn Python from scratch. \
                Please provide clear instructions on Python concepts, best practices and syntax \
                Help create a path of learning for users to be able to create real life, production ready python applications. '

}]

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
