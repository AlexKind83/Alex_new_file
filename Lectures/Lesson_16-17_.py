# Урок 16

# #
# # map(func, *iterables)   map - это цикл
#
# def mult(t):
#     return t * 2
#
#
# lst1 = [2, 8, 12, -5, -10]
#
# lst2 = list(map(mult, lst1))
# print(lst2)
#
# # 2 используем lambda
#
# lst1 = [2, 8, 12, -5, -10]
#
# lst2 = list(map(lambda t: t * 2, lst1))
# print(lst2)


# #
# #
# t = (2.88, - 1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
#
# # 2 убираем lambda и вместо функций передаем тип класса для преобразования
#
# t = (2.88, - 1.75, 100.55)
# t2 = tuple(map(str, t))
# print(t2)


# #
# #
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)


# #
# # Задача
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


# #
# # filter работает как цикл только работает с условием
#
# t = ('abcd', 'abc', 'asdfq', 'def', 'grt')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


# #
# #
#
# b = [66, 90, 68, 59, 76, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# #
# #
#
# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)
#
# # 2
#
# n = [x ** 2 for x in range(10) if x % 2]
# print(n)


# #
# # Задача
#
# import random
#
# my_list = [random.randint(1, 40) for i in range(20)]
#
# print(my_list)
# print(list(filter(lambda num: (num >= 10) and (num <= 20), my_list)))


# # Функцию передаем в качестве аргумента вторую функцию
# #
#
# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# # Вызываем функцию под другим именем
# #
# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())


# # Функция 'декоратор' (старый способ)
# # Функция с использованием замыкания (аргумент функция внутри wrap)
# #
# def my_decorator(func):
#     def wrap():
#         print("Код до функций")
#         func()
#         print("Код после функций")
#     return wrap
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()
#
#
# # 2 Как сейчас используют функцию 'декоратор'
# Функция с использованием замыкания (аргумент функция внутри wrap)
#
# def my_decorator(func):
#     def wrap():
#         print("Код до функций")
#         func()
#         print("Код после функций")
#     return wrap
#
#
# @my_decorator
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# func_test()


# #
# # Функция декоратор (однажды вызванная может вызыватся хоть сколько)
#
# def my_decorator(func):
#     def wrap():
#         print("Код до функций")
#         func()
#         print("Код после функций")
#     return wrap
#
#
# @my_decorator
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# func_test()
# hello()


# # декораторов может быть много, но важна в какой последовательности они применяются
# #
# def bold(fn):
#     def wrap():
#         return '<b>' + fn + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn + '</i>'
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'
#
#
# print(hello())


# # Задача
# #
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функций:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()
#
# # 2 Тоже самое только по другому
#
# def cnt(fn):
#     count = 0
#
#     def wrap(arg1, arg2):
#         nonlocal count
#         count = count + 1
#         print("Вызов функций:", count)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @cnt
# def hello(a, b):
#     print('Hello,', a, '\nHello,', b)
#
#
# hello('Python', 'JavaScript')
# hello('one', 'wto')


# # Разобраться
# #
# def args_decoration(fn):
#     def wrap(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#     return wrap
#
#
# @args_decoration
# def print_data(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")


# # Когда в функцию декоратор нужно добавить аргумент РАЗОБРАТЬСЯ
# # Нужно создать в декорируемой функций еще одну декорируемую функцию с аргументами
# #
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(7, 2)


# # Задача РАЗОБРАТЬСЯ
# #
# def multiply(arg):
#     def test(fn):
#         def wrap(x):
#             return fn(x) * arg
#         return wrap
#     return test
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))







# Урок 17


# #
# #
# print(int('100', 2)) # 4
# print(int('100', 8)) # 64
# print(int('100', 10)) # 100
# print(int('100', 16)) # 256
#
# print(bin(18))  # 0b10010   префикс 0b
# print(oct(18))  # 0o22      префикс 0o
# print(hex(18))  # 0x12      префикс 0x
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0b10010 + 0o22 + 0x12 + 18)


# #
# #
#
# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3) # умножать на отрицательное число можно, но мы не увидим результата
# # print('y' in e)
# # print('y1' in e)
# # print(e[-6])
# # print(e[:4])
# # print(e[::-1])
# # print(e[::])
#
# e = e[:3] + 't' + e[4:]  # как можно добавить в строку t
# print(e)


# # Задача
# #
# def changeCharToStr(s, c_old, c_new):
#     s2 = ''
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, 'N', 'P')
# print('str1 =', str1)
# print('str2 =', str2)


# Используем префикс r
#
# print('Привет')
# print(u'Привет')

# print("C:\\folder\\file.txt\\")
# print(r"C:\folder\file.txt\\"[:-1]) # r"" строка помогает избежать экранирование
# print(R"C:\folder\file.txt" + "\\") # r"" строка помогает избежать экранирование


# Используем f"" строку
#
# name = 'Дмитрий'
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет.")
# m = 2.58976415
# print(f"Число: {round(m, 2)}")
# print(f"Число: {m: .2f}")  # в f'' строке можно не использовать round


# # Используем f'' строку, и второй длинный вариант для сравнения
# #
# x = 10
# y = 5
#
# # print('x = ', x, ', y = ', y, sep='')
# # print(f"{x = }, {y = }")
#
# print(f"{x} x {y} / 2 = {x * y / 2}")
#
# num = 74
# print(f"{{{num}}}")  # {{}} двойные фигурные скобки дают нам имя переменной, и так далее


# # Используем сочетание fr префикс
# #
# dir_name = "my_doc"
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


# #
# #
# s = """
# Многострочный новый
# текст
# """
# print(s)  # без переменной будет пояснение (используется для пояснения функций)
#
# s1 = '''
# Многострочный
# текст
# '''
# print(s1)


# # Документация используемая в 3 кавычках
# #
# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)
# print(min.__doc__)
# print(len.__doc__)


# # Документация должна быть ТОЛЬКО первой строкой
# #
# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: Положительное число, радиус основания цилиндра
#     :param h: Положительное число, высота цилиндра
#     :return: Положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# # Выводит индекс кода union code
# #
# print(ord('a'))  # 97
# print(ord('й'))  # 1081
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# # Задача
# #
# """Выводим ASCII code добавляя ord к x
# arr = [int(sum(arr) / len(arr))] + arr  # Без метода добавляем в начала списка сумму
# строка 499: # Добавляем с помощью диапазона (чтобы добавилось только 3 символа) и если элем. нет то его добавляем
# """
# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr  # Без метода добавляем в начала списка сумму
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


#
#
# print(chr(97))
# print(chr(1048))
# print(chr(8364))

# print(("apple" == "Apple"))  # 97 == 67 False
# print(("apple" > "Apple"))  # 97 > 65 True
# print(ord("a"))
# print(ord("A"))
