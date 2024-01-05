import sqlite3

conn = sqlite3.connect('UsersData.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        User TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")

print("Conectado ao Banco de Dados")