from openai_module import chat_generate_text
from helper_function import get_weather

city = 'Bangalore'
current_weather = get_weather(city)

prompt = f"""
Should I carry an umbrella going out in {city} based on the 
current weather conditions : {current_weather}?
"""
response = chat_generate_text(prompt, model= "gpt-4o" )

print(response)