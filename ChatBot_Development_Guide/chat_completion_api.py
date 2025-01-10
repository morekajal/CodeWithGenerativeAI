from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
            "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write me a 2 paragraph bio on chat-gpt"
        }
    ],
    temperature=0.5,
    max_tokens=50
)

print(completion.choices[0].message)
# print(completion.choices[0].message.content)