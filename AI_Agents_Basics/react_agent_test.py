from openai_module import chat_generate_text
from helper_function import get_weather
from prompts import react_system_prompt


prompt = f"""
Should I carry an umbrella going out in Arizona based on the 

"""
response = chat_generate_text(prompt, model= "gpt-4o" , system_prompt=react_system_prompt)

print(response)