# https://github.com/egoingsb/dae-gu-ai-2-12132


import sqlite3
connect = sqlite3.connect('data.db')
cursor = con1.cursor()
cursor.execute('''
    CREATE TABLE topics (
        id        INTEGER      PRIMARY KEY AUTOINCREMENT,
        title     VARCHAR (50) NOT NULL,
        body      TEXT
    )
''')
cursor.close()
connect.close()