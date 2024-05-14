""""""
import json

# # Урок 35
#
# # Продолжаем Задание урока 34
# #
# #
# class CountryCapital:
#     @staticmethod
#     def load(file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#         finally:
#             return data
#
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         data[new_country] = new_capital
#
#         with open(file_name, 'w', encoding="utf-8") as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print({k.capitalize(): v.capitalize() for k, v in json.load(f).items()})
#
#     @staticmethod
#     def delete_country(file_name):
#         del_country = input("Введите название страны: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(file_name, 'w') as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def search_data(file_name):
#         country = input("Введите название страны: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             print(f"Страна {country.capitalize()} столица {data[country].capitalize()} есть в словаре")
#         else:
#             print(f"Страны {country.capitalize()} нет в словаре")
#
#     @staticmethod
#     def edit_data(file_name):
#         country = input('Введите страну для корректировки: ').lower()
#         new_capital = input('Введите новое название столицы: ').lower()
#
#         # try:
#         #     data = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             data[country] = new_capital
#             with open(file_name, 'w') as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#
# file = "list_capital.json"
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск даннах\n"
#                   "4 - редактирование даннах\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введен некорректный номер")


"""Берем данные json из сторонних ресурсов"""

# pip install requests (установить)

import requests

# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(type(response.text))  № Получаем строку
# # print(response.text)
#
# todos = json.loads(response.text)
# # print(type(todos))  # Получаем список
# # print(type(todos[0]))  # Теперь можем, обратится по индексу (содержит тип класса dict)
# # print(todos)
#
#
# # Переходим к практике.
#
#
# todos_by_user = {}
#
# for todo in todos:  # Ищем сколько и какой пользователь выполнил задач.
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# # Сортируем пользователей по количеству выполненных задач
# print(top_users)
#
# max_completed = top_users[0][1]  # Тут находим максимальное количество выполненных задач
# print(max_completed)
#
# """Этот код надо внедрить (Заменяет первых 2 решения)"""
# # top_complete = max(todos_by_user.values())
# # top_users = [user for user in todos_by_user.items() if user[1] == top_complete]
# # print(top_users)
#
# users = []
# for user, num_complete in top_users:  # Распаковка dict (Записать пример)
#     if num_complete < max_completed:
#         break
#     users.append(str(user))  # Переводим список в строку, чтобы работала строка (max_users = ' and '.join(users))
# print(users)
#
# max_users = ' and '.join(users)
#
# m = 's' if len(users) > 1 else ''  # Здесь создаем условие если пользователей больше чем 1, то добавляем (s)
# print(f"users {max_users} completed {max_completed} TODOs")  # Добавляем или убираем в user(s)
#
#
# def keep(todo):  # Тут создается функция для, сохранение пользователей с максимальным выполненным решением
#     is_complete = todo['completed']
#     has_num_count = str(todo['userId']) in users
#     return is_complete and has_num_count
#
#
# with open('filter.json', 'w', encoding='UTF-8') as f:
#     filter_todos = list(filter(keep, todos))
#     json.dump(filter_todos, f, indent=2)


"""Формат  CSV = Переменные разделенные запятыми"""

import csv

with open('data.csv', encoding='UTF-8') as f:
    file_reader = csv.reader(f, delimiter=';')
    # если в тексте загружаемого файла используется запятая, то указывать не надо (delimiter=';')
    count = 0
    for row in file_reader:  # обязательно нужно распаковывать чтобы
        if count == 0:
            print(f"Файл содержит столбцы: {', '.join(row)}")
        else:
            print(f"{row[0]} - {row[1]}. Родился в {row[2]}")
    count += 1
