from google.auth.transport.requests import Request
import google.generativeai as genai
import vertexai

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")

genai.configure(api_key=API_KEY)

# Initialize vertex ai
vertexai.init(project=PROJECT_ID,
              location=LOCATION)

