from openai_module import chat_generate_text, generate_text_with_conversation
from helper_function import get_weather
from prompts import react_system_prompt
from json_helpers import extract_json

available_actions = {
    "get_weather": get_weather
}

prompt = """
Is it a good day to visit beach in goa?"""

messages = [
    {"role": "system", "content": react_system_prompt},
    {"role": "user", "content": prompt}
]

turn_count = 1
max_turns = 5

while turn_count <= max_turns:
    print(f"Loop: {turn_count}")
    print("-------------------")
    turn_count += 1

    # Generate the response
    response = generate_text_with_conversation(messages, model="gpt-4o")
    print(f"Raw response: {response}")  # Debug the raw response

    # Extract text from the response
    if isinstance(response, dict):
        if "choices" in response:
            text_response = response["choices"][0].get("message", {}).get("content", "")
        else:
            raise TypeError("Unrecognized dictionary structure in response.")
    elif hasattr(response, 'content'):
        text_response = response.content
    elif isinstance(response, str):
        text_response = response
    else:
        raise TypeError("The response object does not contain 'content' in a recognizable format.")

    print(f"Response from the model: {text_response}")

    # Pass the extracted text content to extract_json
    json_function = extract_json(text_response)
    print(f"Extracted JSON Functions: {json_function}")

    if json_function:
        function_name = json_function[0]['function_name']
        function_params = json_function[0]['function_params']
        if function_name not in available_actions:
            raise Exception(f"Unknown action: {function_name}: {function_params}")
        print(f" -- running {function_name} {function_params}")
        action_function = available_actions[function_name]
        result = action_function(**function_params)
        function_result_message = f"Action_Response: {result}"
        messages.append({"role": "assistant", "content": function_result_message})
        print(function_result_message)
    else:
        break
