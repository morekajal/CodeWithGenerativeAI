from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# list to append and maintain chat history w.r.t user input and assistance output
chat_log = []

while True:

    user_input = input()
    #create condition to stop while loop
    if user_input.lower() == 'stop':
        break

    chat_log.append({'role': 'user', 'content': user_input})
    
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=chat_log,
    temperature=0.5, 
    max_tokens = 50
    )

    bot_response = response.choices[0].message.content
    chat_log.append({'role':'assistant', 'content':bot_response})
    
    print(bot_response)

# Save the chat log to a text file
with open("chat_log.txt", "w", encoding="utf-8") as file:
    for entry in chat_log:
        file.write(f"{entry['role'].capitalize()}: {entry['content']}\n")

print("Chat log saved as 'chat_log.txt'.")