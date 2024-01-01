# Урок 13
#
# d = {'a': 1, 'c': 3, 'b': 2}
#
# d1 = {'r': 7, 'q': 40}
# d.update(d1)
# d2 = [('a', 20), ('b', 9)] # {'a': 20, 'b': 9}
# d.update(d2)
# print(d)


# # Задача
# #
# x = {
#     'a': 1,
#     'b': 2
# }
#
# y = {
#     'b': 3,
#     'c': 4
# }
# new_dict = x.copy()
# new_dict.update(y)
# print(new_dict)

# # 2
# x = {
#     'a': 1,
#     'b': 2
# }
#
# y = {
#     'b': 3,
#     'c': 4
# }
#
# new_dict = x | y
# print(new_dict)


# # Обращаемся к ключу 1 уровня и к ключу 2 уровня
# #
# a = {
#     'first': {
#         1: 'one',
#         2: "two",
#         3: 'three',
#     },
#     'second': {
#         4: 'four',
#         5: 'five',
#     },
# }
# print(a)
# for x in a:
#     print(x)
#     # print(a[x])
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y],  sep='')


# # Задача РАЗОБРАТСЯ
# # Работа со вложенными словарями
# #
# sales = {'John': {'N': 3056, 'S': 5463, 'E': 8441, 'W': 2694},
#          'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#          'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#          'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451},
#          }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep='')
#
# person = input('Имя: ')
# region = input('Регион: ')
# print(sales[person][region])
#
# new_data = int(input("Новое значение: "))
#
# sales[person][region] = new_data
# print((sales[person]))


# # Можно ключ и значение поменять местами
# #
# d = {'N': 3056, 'S': 5463, 'E': 8441, 'W': 2694}
# new_d1 = {key: value for key, value in d.items()}
# new_d2 = {value: key for key, value in d.items()}
# d.update({value: key for key, value in d.items()})
#
# print(new_d1)
# print(new_d2)
# print(d)


# # Задача
# #
# d = {'E': 3, 'N': 1, 'S': 2, 'W': 4}
# new_d = {k: v for k, v in d.items() if v <= 2}
# print(new_d)
#
# value = list(d.values())
# print(value)
#
# value = list(d)
# print(value)


# # Задача
# #
# a = ['one', 1, 2, 3, 'two', 'three', 15, 36, 60, 'four', -20]
#
# d = {}
# current_key = ''
#
# for item in a:
#     if type(item) is str:
#         d[item] = []
#         current_key = item
#     else:
#         d[current_key].append(item)
#
# print(d)
#
# # 2
# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# my_dict = dict()
# for i in range(len(a)):
#     if type(a[i]) is str:
#         my_dict[a[i]] = []
#         for j in range(i + 1, len(a)):
#             if type(a[j]) is int:
#                 my_dict[a[i]].append(a[j])
#             else:
#                 break
# print(my_dict)


# # Атрибут zip
# #
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(b, a)}
# print(f)


# #
# #
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# c = zip(a, b)
# c1 = dict(zip(a, b))
# c2 = list(zip(a, b))
# c3 = tuple(zip(a, b))
# c4 = set(zip(a, b))
#
# print(c)
# print(c1)
# print(c2)
# print(c3)
# print(c4)


# # Объединить 2 словаря, нужно отделить круглыми скобками
# #
# d_one = {'name': 'Igor', 'last_name': 'Petrov', 'job': 'Consultant'}
# d_two = {'name': 'Irina', 'last_name': 'Irisova', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(d_one.items(), d_two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)


# # * Перед значением -- распаковка
# #
# d = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*d)
# print(a)
# print(b)


# # sorted сортирует любые типы данных
# #
# a = ('two', 'one', 'three')
# b = (3, 2, 1)
#
# d = dict(zip(a, b))
# print(d)
#
# s = sorted(d.items())
# print(dict(s))
# print(s)


# # ** распаковывает словари
# #
# one = {'apple': 0.45, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# # # print(({**one, **two})) # {'apple': 0.45, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}
#
# print({**two, **one})
#
# for k, v in {**two, **one}.items():
#     print(k, '->', v)


# # Атрибут enumerate() --
# #
# data = ['red', 'green', 'blue']
# num = 1
#
# for val in data:
#     print(num, ') ', val, sep='')
#     num += 1
#
# print()
# for num, val in enumerate(data, start=1):
#     print(num, ') ', val, sep='')






# Урок 14
#


# # Распаковка вложенного списка с помощью *
# #
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# # Используем в функций (*args)
# #
# def func(*args):
#     return args
#
#
# print(func(2))
# print(func(2, 3, 4, 'abc'))
# print(func())


# # Подсчет суммы используя *
# #
# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print((summa(1, 2, 3, 4, 5, 6, 7, 8, 9)))
# print(summa(3, 4, 5))


# # Задача РАСМОТРЕТЬ
# #
# def to_dict(*args):
#     return {element: element for element in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


# # Задача
# #
# def func(*args):
#     midle = sum(args) / len(args)
#     print(midle)
#     res = []
#     for element in args:
#         if element < midle:
#             res.append(element)
#     return res
#
#
# first = func(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(first)
# second = func(3, 6, 1, 9, 5)
# print(second)


# #
# #
# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 4, 5, 6, 7))


# #
# #
# def print_score(student, *scores):
#     print('Student Name:', student)
#     for score in scores:
#         print(score)
#
#
# print_score('Irina', 5, 4, 3, 3, 5)
# print_score('Igor', 5, 4, 5, 2, 5)
# print_score('Lev')


# # Свойства ** передает dict(словарь)
# #
# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(b=9))


# #
# #
# def intro(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print()
#
#
# intro(name='Irina', surname='Reznikova', aga=22)
# intro(name='Igor', surname='Berukov', email='igor@mail.ru', aga=25, phone='+7909999-46-89')


# # Задача РАСМОТРЕТЬ
# #
# def db(**kwargs):
#     my_dict.update(kwargs)
#     # print("внутри функций:", id(my_dict))
#
#
# my_dict = {'one': 'first'}
# # print(id(my_dict))
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', aga=31, wight=61, eyes_color='grey')
# print(my_dict)


# # Последовательность (*, **, именованные и позиционный аргумент)
# # Именованные аргументы в ВЫЗОВЕ можно ставить где угодно, НО не в * и позиционных
# #
# def func(a, b, c, *args, d, e, **kwargs):
#     return a, b, c, args, e, kwargs, d
#
#
# print(func(5, 9, 7, 8, 4, 3, 2, 1, k1=22, k2=31, e=100, k3=11, k4=91, d=55))


# # Области видимости
# #
# name = 'Tom'
# # print("глобальная область видимости: ", id(name))
#
#
# def hi():
#     global name
#     name = 'Sam'
#     # print("локальная область видимости: ", id(name))
#     surname = "Johnson"
#     print('Hello', name, surname)
#
#
# def bye():
#     print(("Goog bye", name))
#
#
# print(name)
# hi()
# bye()
# print(name)
# # print("глобальная область видимости: ", id(name))


# #
# #
# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()


# # Вложенные функций
# # РАЗАБРАТСЯ области видимости
# #
#
#
# # x = 4
#
#
# def add_five(a):
#     x = 2
#
#     def add_some():
#         # x = 1
#         print('x =', x)
#         return a + x
#
#     return add_some()
#
#
# print(add_five(5))


#
# # Когда зарезервированные Функций перестают работать
# #
# sum = 5
#
# lst = [9, 5, 8, 7, 6]
# print(sum(lst)) # 5([9, 5, 8, 7, 6])


# # Вывод зарезервированных Функций
# #
# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)
