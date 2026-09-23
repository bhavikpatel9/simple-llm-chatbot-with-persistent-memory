
import sqlite3

connection = sqlite3.connect("chatbot.db")
cursor = connection.cursor()

cursor.execute("""
    ALTER TABLE conversations
    ADD COLUMN summarized_through_message_id INTEGER DEFAULT 0
""")

connection.commit()
connection.close()

print("Summary checkpoint column added.")