from google import genai
from dotenv import load_dotenv
import os

from summary_manager import summarize_eligible_messages
from database import (
    get_summary,
    get_summary_checkpoint,
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = "gemini-3.8-flash"

conversation_id = 1

old_checkpoint = get_summary_checkpoint(conversation_id)

print("Checkpoint before:", old_checkpoint)

result = summarize_eligible_messages(
    client,
    model,
    conversation_id,
)

print("Function result:", result)
print("New checkpoint:", get_summary_checkpoint(conversation_id))
print("Saved summary:", get_summary(conversation_id))

print("TEST COMPLETED")