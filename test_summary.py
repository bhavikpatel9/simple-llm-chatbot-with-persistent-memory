
# from dotenv import load_dotenv
# from google import genai
# import os

# from summary_manager import generate_summary
from database import get_summary, update_summary

# # Load API key from .env
# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     raise ValueError("GEMINI_API_KEY was not loaded")

# client = genai.Client(api_key=api_key)

# MODEL = "gemini-3.8-flash"

# # Use an existing conversation ID from your database.
conversation_id = 5

# # Simulate some older conversation messages.
# old_messages = [
#     ("user", "My name is Bhavik."),
#     ("assistant", "Hello Bhavik! Nice to meet you."),
#     ("user", "I am learning Python and building an AI chatbot."),
#     ("assistant", "That sounds like a useful project."),
#     ("user", "I want to become an AI Application Engineer."),
#     ("assistant", "You can build skills in LLM APIs, RAG, and deployment.")
# ]

# # 1. Get any existing summary
# old_summary = get_summary(conversation_id)

# print("\nPrevious summary:")
# print(old_summary or "(No previous summary)")

# # 2. Generate an updated summary using Gemini
# new_summary = generate_summary(
#     client=client,
#     model=MODEL,
#     old_summary=old_summary,
#     old_messages=old_messages
# )

# print("\nGenerated summary:")
# print(new_summary)

# # 3. Save the summary to SQLite
# update_summary(conversation_id, new_summary)

# print("\nSummary saved.")

# 4. Retrieve it again from SQLite
saved_summary = get_summary(conversation_id)

print("\nRetrieved summary:")
print(saved_summary)

# 5. Verify persistence
# if saved_summary == new_summary:
#     print("\nTEST PASSED: Summary was saved and retrieved.")
# else:
#     print("\nTEST FAILED: Summary does not match.")