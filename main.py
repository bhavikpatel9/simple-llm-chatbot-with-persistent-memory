from google import genai
from dotenv import load_dotenv
import os
import json

from database import save_message, get_messages


load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break;

    save_message("user", user_input)

    stored_messages = get_messages()

    conversation = []

    for role, content in stored_messages:
        conversation.append({
            "role": role,
            "content": content
        })

    json_string = json.dumps(conversation)
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=json_string
    )
    print("AI:", interaction.output_text)

    save_message('assistant', interaction.output_text)