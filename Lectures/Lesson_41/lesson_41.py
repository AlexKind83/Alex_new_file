"""3 метода вывода данных из БД.
   Много табличные запросы."""

# Урок 41

import sqlite3

with sqlite3.connect('db_4.db') as con:
    cur = con.cursor()
    cur.execute("""
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 2, 5;
    """)

    # res = cur.fetchall()  # В виде списка картежей.
    # print(res)
    #
    # for res in cur:
    #     print(res)

    # res = cur.fetchone()  # Вывести одну первую запись
    # print(res)
    #
    # res1 = cur.fetchmany(2)  # Тут можно вывести сколько строк можем вывести
    # print(res1)
    #
    # res2 = cur.fetchall()  # В виде списка картежей.
    # print(res2)
