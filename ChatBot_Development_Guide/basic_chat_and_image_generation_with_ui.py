# you can change the command as per file_name to run the FastAPI app
from openai import OpenAI
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

chat_responses = []   # to keep our chat history alive on UI


chat_log = [{'role' : 'system',
             'content' : 'You are a Python tutor AI, completely dedicated to teach users how to learn Python from scratch. \
                Please provide clear instructions on Python concepts, best practices and syntax \
                Help create a path of learning for users to be able to create real life, production ready python applications. '

}]

# chat_responses = []

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    # return templates.TemplateResponse("layout.html", {"request":request})
    return templates.TemplateResponse("home.html", {"request":request, "chat_responses":chat_responses})


@app.post("/", response_class=HTMLResponse)
async def chat(request:Request, user_input: Annotated[str, Form()]):

    chat_log.append({'role': 'user', 'content': user_input})
    chat_responses.append(user_input)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=chat_log,
    temperature=0.5, 
    max_tokens = 50
    )

    bot_response = response.choices[0].message.content
    chat_log.append({'role':'assistant', 'content':bot_response})
    chat_responses.append(bot_response)

    # return bot_response
    return templates.TemplateResponse("home.html", {"request":request, "chat_responses":chat_responses})

@app.get("/image", response_class=HTMLResponse)
async def image_page(request: Request):
    return templates.TemplateResponse("image.html", {"request":request})

@app.post("/image", response_class=HTMLResponse)
async def create_image(request: Request, user_input: Annotated[str, Form()]):

    response = client.images.generate(
    model="dall-e-3",
    prompt=user_input,
    size="1024x1024",
    # quality="standard",
    n=1,
)

    image_url = response.data[0].url
    return templates.TemplateResponse("image.html", {"request":request, "image_url":image_url})


# http://127.0.0.1:8000/  : for chat
# http://127.0.0.1:8000/images : for images