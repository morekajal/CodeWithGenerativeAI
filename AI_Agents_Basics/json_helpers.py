import re
import json
from pydantic import BaseModel, ValidationError
from typing import get_type_hints

def model_to_json(model_instance):
    """
    Converts a Pydantic model instance to a JSON string.

    Args:
        model_instance (YourModel): An instance of your Pydantic model.

    Returns:
        str: A JSON string representation of the model.
    """
    return model_instance.model_dump_json()

def extend_search_new(text, span):
    start, end = span
    nest_count = 1  # Starts with 1 since we know '{' is at the start position
    for i in range(end, len(text)):
        if text[i] == '{':
            nest_count += 1
        elif text[i] == '}':
            nest_count -= 1
            if nest_count == 0:
                return text[start:i+1]
            
    return text[start:end]


def extract_json(text_response):
    pattern = r'\{.*?\}'
    matches = re.finditer(pattern, text_response, re.DOTALL)
    json_objects = []

    for match in matches:
        json_str = extend_search_new(text_response, match.span())
        try:
            json_obj = json.loads(json_str)
            json_objects.append(json_obj)
        except json.JSONDecodeError:
            continue

    return json_objects if json_objects else None