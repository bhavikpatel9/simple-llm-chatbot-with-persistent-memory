from database import (
    get_messages_to_summarize,
    get_summary_checkpoint,
)

conversation_id = 1

messages = get_messages_to_summarize(
    conversation_id,
    keep_recent=10,
)

checkpoint = get_summary_checkpoint(conversation_id)

print("Checkpoint:", checkpoint)
print("Eligible messages:")

for message in messages:
    print(message)

assert all(message[0] > checkpoint for message in messages)

print("TEST PASSED")