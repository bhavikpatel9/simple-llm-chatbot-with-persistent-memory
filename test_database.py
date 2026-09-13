from database import (
    create_database,
    create_conversation,
    save_message,
    get_messages
)


create_database()

conversation_1 = create_conversation("Python Learning")
conversation_2 = create_conversation("Travel Planning")

save_message(
    conversation_1,
    "user",
    "What is Python?"
)

save_message(
    conversation_1,
    "assistant",
    "Python is a programming language."
)

save_message(
    conversation_2,
    "user",
    "Plan a trip to Japan."
)

print("Conversation 1:")
print(get_messages(conversation_1))

print("\nConversation 2:")
print(get_messages(conversation_2))