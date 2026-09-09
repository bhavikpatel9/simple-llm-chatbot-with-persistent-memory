import sqlite3

connection = sqlite3.connect("chatbot.db")

cursor = connection.cursor()

cursor.execute("""
    SELECT id, role, content
    FROM messages
    ORDER BY id
""")

messages = cursor.fetchall()

for message in messages:
    print(message)

connection.close()