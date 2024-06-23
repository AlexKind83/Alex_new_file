cd
# Урок 9


# # Типы аргументов функций
# #
# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# # Задание (14:50)
# #
# def set_param(c=20, s='-'):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(5, '*')
# set_param(s='#')


# # Задача (22:05) РАСМОТРЕТЬ -- 2 параметра, и второй сравнивает на True или False
# #
# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         print(current)
#         if even and current % 2 == 0:
#             s += current
#         elif not even and current % 2:
#             s += current
#         # print(n)
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("\nСумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# #
# def display_info(name, age):
#     print('Name:', name, '\nAge', age)
#
#
# display_info('Ira', 23)
# display_info(23, 'Ira')
# display_info(age=23, name='Ira')
# display_info('Igor', age=23, name='Ira') # TypeError


# #
# # Изменяемые и неизменяемые Объекты
# #
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2) # True
# print(lt1 is lt2) # False
#
# a = 'Hello'
# b = 'Hello'
# print(id(a))
# print(id(b))
# print(a == b) # True
# print(a is b) # True
#
# n = 5
# m = 5
# print(id(n))
# print(id(m))
# print(n == m) # True
# print(n is m) # True


# #
# # Кортеж (tuple)
# #
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# # 72
# # 48


# # Создание пустого кортежа
# #
# a = ()
# b = tuple()
# print(type(a))
# print(type(b))
# print(a)
# print(b)


# #
# a = (5,) # Чтобы число не было int а было кортежам нежна запятая после числа
# print(type(a))
# print(a)


# # Записи кортежей
# #
# n = 'Hello', 'Python' # или ['Hello', 'Python']
# b = tuple(['Hello', 'Python']) # или b =tuple(('Hello', Python'))
# print(type(b))
# print(b)


# #
# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(a[3]) # 4
# print(a[1:3]) # (2, 3)
# # a[1] = 3 # не работает -- TypeError


# #
# # Генератор кортежа
# #
# from random import randint
# s = tuple(i for i in range(5))
# print(s)
#
# c = tuple(int(input('-> ')) for i in range(5))
# print(c)
#
# d = tuple(randint(0, 100) for i in range(5))
# print(d)


# # Задача (2:03:08)
# #
# s = tuple(2 ** i for i in range(1, 13))
# print(s)


# #
# t1 = tuple('Hello')
# t2 = tuple('World')
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t1 * 2)
# print(t3)
#
# print(t3.count('l'))
# if 'e' in t3:
#     print(t3.index('e'))


# # Пробежаться в цикле по кортежу
# #
# t1 = tuple('Hello')
# t2 = tuple('World')
# t3 = t1 + t2
#
# for i in t3:
#     print(i, end=' ')


# # Задача (2:18:57) РАСМОТРЕТЬ решение срезов используя параметры функций
# #
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             a = tpl.index(el) # Поиск индекса первой 8
#             b = tpl.index(el, a + 1) # После как найдет первую 8, пойдет искать второю
#             return tpl[a:b + 1]
#         else:
#             return tpl[tpl.index(el):] # tpl[2:]
#     else:
#         return tuple() # или просто ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
#
#
# # 2 Вариант
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             return tpl[tpl.index(el): tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):] # tpl[2:]
#     else:
#         return tuple() # или просто ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# # Меняем значение списка внутри кортежа
# #
# t = (10, 11, [1, 2, 3], [4, 5, 6], ['Hello', 'World'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))


# #
# # Распаковка кортежа
# #
#
# # 1 Вариант
#
# # t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# # print(x, y, z)
#
# # 2 Вариант
#
# t = (1, 2, 3)
# x, y, z = t # Распаковка кортежа
# print(x, y, z) # 1, 2, 3


# # Через функцию создали кортеж
# #
# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # 1
# #
# first_name, year, married = get_user() # Распаковка из функций кортежа
# print(first_name, year, married)
#
# # 2
# #
# # user = get_user()
# # print(user)
# # first_name, year, married = user # Распаковка кортежа
# # print(first_name, year, married)
#
# # 3
# #
# # print(user[0])
# # print(user[1])
# # print(user[2])







# Урок 10


# # Изменяем картеж
# #
# tpl = (1, 2, 3, 4, 5, 6)
# print(tpl)
# lst = list(tpl)
# print(lst)
# ptl1 = tuple(lst)
# print(ptl1)
# del ptl1
# # print(ptl1)


# # Вложенный картеж (распаковываем)
# #
# countries = (
#     ('Германия', 80.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6))),
# )
# print(countries, end='\n\n')
#
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nСтрана:', country_name, 'население =', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород:', city_name, 'население =', city_population)


#
# GitHub (Гид хаб)
#
# Система контроля версий (version Control Systems, VCS) -- это система,
# сохраняющая изменения в одном или нескольких файлах так,
# чтобы потом можно было восстановить определённые старые версий.
#
#
# git --version(Вэршен)
# Проверка Версия GitHub
#
# git --help(Хелп)
# Информация о наборе команд GitHub
#
#
# git init
# Создание репозитория (применяют один раз для одного репозитория)
#
#
# git status
# Проверка статуса репозитория (в каком, состояний находится наш репозиторий)
#
#
# git add -A
#         -A, --all -- (вносит в репозиторий) все файлы, которые находятся в папке и во всех подпапках
#         mail.py -- Добавляем в репозиторий конкретный файл, папку.
#         . -- (Из текущей директорий) Добавляет в репозиторий все не добавленные файлы, папки
#
# git config --global user.name 'Имя которое сами придумали(имя пользователя репозитория)
# git config --local (?) 1:01:35 (Урок 010) (каждый раз нужно создавать новое имя)
#
# git config --global user.email 'создаешь имя емайла'
#
# git commit -m 'Название самого комита' (Название нужно делать понятным (что мы в этом комите сохраняли, храним)
# создается контрольная точка (отправка всех данных под версеонный контроль).
#
#
# Создание отдельных веток, и переход на другие ветки
#
# git branch
# Посмотреть на какой ветки мы находимся
#
# git branch название создаваемой ветки
# Создаем, новую ветку и даем название
#
# git branch -D "название удаляемой ветки"
# удаляем ветку по её названию
#
# git checkout имя ветки на которую переходим.
# Переходим на другую ветку по её названию
#
# git merge название ветки которую хотим слить с основной веткой.
# Слияние ветки readme с веткой master
#
#
# История комит
#
# git log
# История комита
