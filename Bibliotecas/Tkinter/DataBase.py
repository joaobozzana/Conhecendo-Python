import sqlite3

conn = sqlite3.connect('UsersData.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        usuario TEXT NOT NULL,
        senha TEXT NOT NULL
    )
""")
