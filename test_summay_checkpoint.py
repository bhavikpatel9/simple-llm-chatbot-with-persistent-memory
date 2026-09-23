
from database import (
    get_summary_checkpoint,
    update_summary_checkpoint
)

conversation_id = 1

# Read the initial checkpoint
checkpoint = get_summary_checkpoint(conversation_id)
print("Initial checkpoint:", checkpoint)

# Simulate having summarized through message ID 20
update_summary_checkpoint(conversation_id, 20)

# Read it again
checkpoint = get_summary_checkpoint(conversation_id)
print("Updated checkpoint:", checkpoint)

assert checkpoint == 20

print("TEST PASSED")