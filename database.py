import sqlite3


def create_database():
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,

            FOREIGN KEY (conversation_id)
            REFERENCES conversations(id)
        )
    """)

    connection.commit()
    connection.close()

# create_database()

def create_conversation(title):
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO conversations (title)
        VALUES (?)
    """, (title,))

    conversation_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return conversation_id   

def save_message(conversation_id, role, content):
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO messages (conversation_id, role, content)
        VALUES (?, ?, ?)
        """,
        (conversation_id, role, content)
    )

    connection.commit()
    connection.close()

def get_messages(conversation_id):
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT role, content
        FROM messages
        WHERE conversation_id = ?
        ORDER BY id
    """, (conversation_id,))

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