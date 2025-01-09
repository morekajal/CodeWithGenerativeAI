import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#Create instance of OpenAI class
# Set the API key for OpenAI
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def chat_generate_text(
        prompt : str,
        openai_api_key: str = None,
        model : str = "gpt-3.5-turbo",
        system_prompt: str = "You are a helpful assistant.",
        temperature : float = 0.4,
        max_tokens : int = 128
        ):

    messages = [
        {"role": "system", "content": f"{system_prompt}"},
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature, 
        max_tokens = max_tokens
    )

    return response.choices[0].message

def generate_text_with_conversation(messages, model = 'gpt-4o'):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content