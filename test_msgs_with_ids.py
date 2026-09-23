from database import get_messages_with_ids

conversation_id = 1

messages = get_messages_with_ids(conversation_id)

for message in messages:
    print(message)

assert all(len(message) == 3 for message in messages)

print("TEST PASSED")