# Now level the agent to think on Action_Response and Answer to form.

from openai_module import chat_generate_text
from helper_function import get_weather
from prompts import react_system_prompt
from json_helpers import extract_json

# Available actions are:
available_actions = {
    "get_weather": get_weather
}

prompt = """
Should I take an umbrella when going out today in London?"""

response = chat_generate_text(prompt, model="gpt-4o", system_prompt=react_system_prompt)

# Ensure the content is extracted from the response object
# To eliminate the error
if hasattr(response, 'content'):
    text_response = response.content  # Extract the content string
else:
    raise TypeError("The response object does not contain 'content' attribute.")

print(f"Response from the model: {text_response}")

# Pass the extracted text content to extract_json
json_function = extract_json(text_response)

print(f"Extracted JSON Functions: {json_function}")

# Uncomment below block to execute the extracted function
if json_function:
    function_name = json_function[0]['function_name']
    function_parms = json_function[0]['function_params']
    if function_name not in available_actions:
        raise Exception(f"Unknown action: {function_name}: {function_parms}")
    print(f" -- running {function_name} {function_parms}")
    action_function = available_actions[function_name]
    # Call the function
    result = action_function(**function_parms)
    function_result_message = f"Action_Response: {result}"
    print(function_result_message)
