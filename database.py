import sqlite3

# connection = sqlite3.connect("chatbot.db")

# cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS messages (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         role TEXT NOT NULL,
#         content TEXT NOT NULL
#     )
# """)

# connection.commit()
# connection.close()

def save_message(role, content):

    connection = sqlite3.connect("chatbot.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO messages (role, content)
        VALUES (?, ?)
        """,
        (role, content)
    )

    connection.commit()
    connection.close()

def get_messages():

    connection = sqlite3.connect("chatbot.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT role, content
        FROM messages
        ORDER BY id
        """
    )

    messages = cursor.fetchall()

    connection.close()

    return messages

    
def get_conversations():
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title
        FROM conversations
        ORDER BY id
    """)

    conversations = cursor.fetchall()

    connection.close()

    return conversations

# create_database()

# conversation_id = create_conversation("Python Learning")

# print("Conversation ID:", conversation_id)

def get_summary(conversation_id):
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT summary
        FROM conversations
        WHERE id = ?
    """, (conversation_id,))

    result = cursor.fetchone()
    connection.close()

    if result is None:
        return ""

    return result[0] or ""

def update_summary(conversation_id, summary):
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE conversations
        SET summary = ?
        WHERE id = ?
    """, (summary, conversation_id))

    connection.commit()
    connection.close()


def get_summary_checkpoint(conversation_id):
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT summarized_through_message_id
        FROM conversations
        WHERE id = ?
    """, (conversation_id,))

    result = cursor.fetchone()
    connection.close()

    if result is None:
        raise ValueError("Conversation not found")

    return result[0] or 0


def update_summary_checkpoint(conversation_id, message_id):
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE conversations
        SET summarized_through_message_id = ?
        WHERE id = ?
    """, (message_id, conversation_id))

    connection.commit()
    connection.close()  

def get_messages_with_ids(conversation_id):
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, role, content
        FROM messages
        WHERE conversation_id = ?
        ORDER BY id ASC
    """, (conversation_id,))

    messages = cursor.fetchall()
    connection.close()

    return messages      

def get_messages_to_summarize(conversation_id, keep_recent=10):
    messages = get_messages_with_ids(conversation_id)

    checkpoint = get_summary_checkpoint(conversation_id)

    # Only messages not already summarized
    unsummarized = [
        message
        for message in messages
        if message[0] > checkpoint
    ]

    # Keep the newest messages out of the summary
    if len(unsummarized) <= keep_recent:
        return []

    return unsummarized[:-keep_recent]