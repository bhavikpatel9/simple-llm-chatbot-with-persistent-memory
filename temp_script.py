import sqlite3

connection = sqlite3.connect("chatbot.db")
cursor = connection.cursor()

cursor.execute("""
    ALTER TABLE conversations
    ADD COLUMN summary TEXT DEFAULT ''
""")

connection.commit()
connection.close()

print("Summary column added.")