""""""

# Урок 40

import sqlite3

with sqlite3.connect('users.db') as con:
    cur = con.cursor()
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+791221138576',
    # age INTEGER CHECK(age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )""")

    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)

    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address1 TEXT NOT NULL DEFAULT 'г. Сочи'
    # """)

    # cur.execute("""
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address;
    # """)


