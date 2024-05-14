import sqlite3

with sqlite3.connect('homework_42.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT,
    name TEXT,
    patronymic TEXT,
    age INTEGER,
    [group] INTEGER,
    FOREIGN KEY ([group]) REFERENCES groups(id) ON DELETE CASCADE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS groups(
    id INTEGER PRIMARY KEY,
    group_name TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS association(
    lesson_id INTEGER,
    group_id INTEGER,
    FOREIGN KEY (lesson_id) REFERENCES lessons(id),
    FOREIGN KEY (group_id) REFERENCES groups(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS lessons(
    id PRIMARY KEY,
    lesson_title TEXT
    )
    """)


