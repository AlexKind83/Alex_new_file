""""""

# Урок 43

import sqlite3

with sqlite3.connect('car.db') as com:
    cur = com.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )
    """)

# con.commit() - сохраняет все изменения в БД
# con.close() -  закрывает соединение с БД
