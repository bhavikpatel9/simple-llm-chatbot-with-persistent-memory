from google import genai
from dotenv import load_dotenv
import os
import json

from database import save_message, get_messages, create_conversation, create_database, get_conversations
from context_manager import build_context


load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

create_database()

# Show existing conversations
conversations = get_conversations()

print("\nYour conversations:")

for conversation_id, title in conversations:
    print(f"{conversation_id}. {title}")

print("0. Start a new conversation")

choice = input("\nChoose a conversation: ")


if choice == "0":

    title = input("Enter conversation title: ")

    conversation_id = create_conversation(title)

else:

    conversation_id = int(choice)


print(f"\nConversation selected: {conversation_id}")
print("Chatbot started. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break;

    save_message(conversation_id, "user", user_input)

    stored_messages = get_messages(conversation_id)

    conversation = build_context(
        client=client,
        model="gemini-3.8-flash",
        messages=stored_messages,
        max_input_tokens=100
    )

    print("\nSelected context:")

    for message in conversation:
        print(message)

    json_string = json.dumps(conversation)
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=json_string
    )
    print("AI:", interaction.output_text)
    print("usage:", interaction.usage)

    save_message(conversation_id, 'assistant', interaction.output_text)