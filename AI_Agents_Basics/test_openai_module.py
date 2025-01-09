from openai_module import chat_generate_text

prompt = 'generate a 5 word sentence'

response = chat_generate_text(prompt)

print(response)