"""CREATE TABLE - создать таблицу
   PRIMARY KEY - создать уникальный ключ
   IF NOT EXISTS - когда документ создан повторный вызов программы создаст ошибку
   чтобы это избежать создается эта запись IF NOT EXISTS.
   AUTOINCREMENT - чтобы не приходилось обновлять постоянно, он будет обновляться автоматически.
   NOT NULL - поле чем то заполнено"""

# Урок 39

"""SQL"""

import sqlite3


# con = sqlite3.connect('profile.db')
# cur = con.cursor()
# cur.execute("""""")
# con.close()

with sqlite3.connect('profile.db') as con:
    cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # summa REAL,
    # date TEXT
    # )""")
    cur.execute('DROP TABLE users')

