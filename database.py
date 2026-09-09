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