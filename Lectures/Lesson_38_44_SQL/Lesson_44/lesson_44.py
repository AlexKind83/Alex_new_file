"""Программно добавляем данные
   Сериализация = это перевод языка sql на язык Python"""

# Урок 44

# import sqlite3
#
#
# with sqlite3.connect('car.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
# # Вносим данные и привязываемся к id что не дает возможность до записи.
# # 1 вариант который, привязывается к id.
#
#     cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
#     cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
#     cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
#     cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
#     cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")


# con.commit() - сохраняет все изменения в БД
# con.close() -  закрывает соединение с БД

# --------------------------------------------------------------------------

# import sqlite3

# # 2 вариант который, дает возможность не привязываться к id

# cars_tpl = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 46000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
# with sqlite3.connect('car.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {"Price": 0})
    # # :Price = придуманный какой-то параметр [Именованный параметр]


# 1 вариант

    # for car in cars_tpl:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)


# # 2 вариант (тут как проход в цикле) = однотипных

#     cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_tpl)


# # 3 вариант (позволяет выполнить больше одного запроса = многотипных)
# # так нельзя прописывать (NULL, ?, ?) нельзя использовать символы % и именованные параметры

    # cur.executescript("""
    # DELETE FROM cars WHERE model LIKE 'B%';
    # UPDATE cars SET price = price + 100;
    # """)

# ----------------------------------------------------------------------------------

# Создаем в БД car таблицу cars
# Здесь мы разбираем возможность executescript работая в tru/except,
# возможность отката до BEGIN если в процессе добавления произошла ошибка

# import sqlite3
#
# con = None  # чтобы не подчеркивалась в finally: [создаем вспомогательную переменную]
# try:
#     con = sqlite3.connect('car.db')
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()  # если корректно отработает весь блок выше то, выполнится сохранение
# except sqlite3.Error as e:
#     if con:
#         con.rollback()  # если будет ошибка, то он откатывает изменения в исходное состояние до строки BEGIN.
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()

# -------------------------------------------------------------------

# К таблице cars добавляем таблицу cost.
# Здесь мы в 1 таблицу вносим данные продаваемого авто,
# и во второй талицы вносим данные продаваемого авто и покупаемого.


# import sqlite3
#
# with sqlite3.connect('car.db') as con:
#     con.row_factory = sqlite3.Row  # обязательно если хотим пройти в цикле
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_row_id = cur.lastrowid  # возвращает последнею строку id [id последней записи]
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

# # вывести данные
#
#     cur.execute("SELECT model, price FROM cars")
#
# # 1
#     # rows = cur.fetchall()
#     # print(rows)
#
# # 2
#     for res in cur:
#         # print(res[0], res[1])
#         print(res['model'], res['price'])

# ----------------------------------------------------------------------

# К таблице cars и cost добавляем таблицу users.
# В эту таблицу помещаем картинку.

# import sqlite3
#
#
# def read_ava(n):
#     """Считывает картинку и сохраняет ее в буфер"""
#     try:
#         with open(f"avatars/{n}.png", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     """Берем картинку из БД и перезаписываем в корневую папку под новым именем"""
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True  # Можно не писать
#
#
# with sqlite3.connect('car.db') as con:
#     con.row_factory = sqlite3.Row  # обязательно если хотим пройти в цикле
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT, ava BLOB, score INTEGER
#     );
#     """)
#
# # # Тут вызываем функцию которая сохраняет картинку в буфер, и она хранится в переменной img.
# # # В условие мы записываем картинку в БД по адресу таблицы users
#     img = read_ava(1)
#     if img:
#         binary = sqlite3.Binary(img)  # Записать метод
#         cur.execute("INSERT INTO users VALUES ('Илья', ?, 1000)", (binary,))
#
# # Берем из таблицы users данные ava, и передаем в функцию write_ava
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)

# --------------------------------------------------------------------------

# Восстанавливаем БД.
# Нужно для того чтобы при удаление БД можно было восстановить.
# БД сохраняются только в формате sql


# import sqlite3

# # Записываем

# with sqlite3.connect('car.db') as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", 'w') as f:
#         for sql in con.iterdump():
#             f.write(sql)
#
# # # Открываем
# # # ДЛя открытия БД нужно создавать новое имя!!!
#
# with sqlite3.connect('car_new.db') as con:
#     cur = con.cursor()
#
#     with open('sql_dump.sql', 'r') as f:
#         sql = f.read()
#         cur.executescript(sql)
