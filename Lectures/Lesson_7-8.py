# 7 УРОК


# # Используем метод copy
#
# a = [1, 2, 3]
# b = a
# print('a =', a)
# print('b =', b)
# a.append(20)
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)


# # Методы reverse, sort
# #
# a = [5, 4, 1, 2, 3]
# print(a)
# a.reverse() # Перестроил списка в обратном порядке
# print(a)
#
# a.sort() # Сортируем элементы списка
# print(a)
# a.sort(reverse=True)
# print(a)


# # Метод sort(key=len)
# #
# b = ["Виталий", 'Сергей', 'Александр', 'Анна']
# b.sort()
# print(b)
# b.sort(key=len)
# print(b)


# # Функция sorted работает с любыми типами данных
# # Не изменяет список, а создает новый список
# #
# a = [5, 4, 1, 2, 3]
# print(a)
#
# sort = sorted(a)
# print(sort)
#
# sort = sorted(a, reverse=True)
# print(sort)


# # Генерация случайных данных, МОДУЛЬ Функция random
# #
# import random
#
# print(random.random())
# print(random.randint(3, 12)) # случайные числа (от a до b)
# print(random.randrange(3, 9, 2)) # ведет себя как range (start, stop, step)
#
# print(round(random.uniform(10.5, 25.25), 2))
#
# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # print(random.choice(city_list))
# # print(random.choices(city_list, k=3))

# random.shuffle(city_list)
# print(city_list)
#
# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 1, 2, 3]
# print(random.choice(s))
# print(random.choices(s, k=5))


# #
# lst = [5, 4, 3, 2, 1]
# print(len(lst))
# print(sum(lst)) # Не работает со строковыми значениями
# print(min(lst))
# print(max(lst))
#
# a = [5, 4, 3, 2, 1]
# res = 0
# for i in a:
#     res += i
# print(res)
# print(sum(a))


# #
# sum_ = 5
# print(sum_)
# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 1, 2, 3]
# print(sum(s))


# # Задача (1:14:00)
# #
# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print('Max:', max_)
# mas.remove(max_)
# mas.insert(0, max_)
# print(mas)


# # Задача (1:42:56)
# #
# import random
#
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
#
# min_ch = min(lst)
# print('min  =', min_ch)
#
# ind_min = lst.index(min_ch)
# print('index min =', ind_min)
#
# print(lst[ind_min:]) # del lst[0: ind_min]


# #
# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
#
# print('a' not in x)
# print('e' not in x)


# # Проверяем пустой или нет список
# # 1  Вариант
# lst = []
# if len(lst) == 0:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")
#
# # 2 Варианте
# if not lst == 0:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")
#
# # 3 Вариант
# lst = []
# print(bool(lst))
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")


# # Задача (1:57:23) РАСМОТРЕТЬ
# #
# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
#
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in b:
#         d.append(element)
# print("Элементы обоих списков без повторений:", d)
#
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Общие элементы для двух списков:", c)
#
# w = [min(a), min(b), max(a), max(b)]
# print("Минимальное и максимальное значение каждого из списков:", w)


# Задача (2:40:29)
# Домашняя


# #
# # Список Матрица
# #
# # 1 Вариант (длинный)
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
#
# # m = ['Hello', 'World'] # Тоже пример списка Матрицы
#
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()
#
# # 2 Вариант (короткий)
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print(m)
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()






# 8 урок

#


#


# Задача
#
# import random
# w, h = 3, 4
# matrix = [[random.randint(-20,10) for x in range(w)]for y in range(h)]
#
# m = 0
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             m += 1
#     print()
#
# print("Количество отрицательный элементов:", m)


# # Вложенные списки
# #
# for x, y in [[1, 2], [3,4], [5,6], [7,8]]:
#     print(x, '+', y, '=', x + y)


# #
# w, h = 4, 3
# matrix = [[input('-> ') for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()


# #
# import math
#
# num1 = math.sqrt(4) # Квадратный корень
# num2 = math.ceil(3.1) # Округляет до ближайшего целого числа
# num3 = math.floor(3.8) #
#
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)


# # ЗАПОМНИТЬ
# # Даем псевдоним import Math # Квадратный корень
# import math as m # Даем псевдоним math
# from math import sqrt, ceil # Тут sqrt можно обращаться без math и ceil
#
# num1 = m.sqrt(4)
# num2 = ceil(3.1)
#
# print(num1)
# print(num2)


# # ЗАПОМНИТЬ
# import time
# import locale # Для того чтобы перевести месяц в русский
#
# seconds = time.time()
# print("Количество секунд:", seconds)
#
# locale_time = time.ctime(1701589958) # в скобках можно поместить дату создания файла
# print("Местное время;", locale_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, '.', res.tm_mon, '.', res.tm_year, sep='')
#
# # print(time.strftime("Today is %B %d, %Y"))
# # print(time.strftime("%d.%m.%Y, %H:%M:%S")) # 2 вариант более удобный
# # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime()))
# print(time.strftime("Сегодня: %B %d, %Y"))
#
# locale.setlocale(locale.LC_ALL, 'ru') # обязательная
# print(time.strftime("Сегодня: %B %d, %Y")) # Перевели на русский месяц
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


#
# Function
#
# print()
#
#
# def hello(name): # аргумент
#     print('Hello', name)
#
#
# hello('Irina') # параметры
# hello('Igor')


# #
# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('abc', 'def')


# # Задание
# def symbol(count, a, b):
#     for i in range(count): # pass # или 3 точки
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')


# #
# def get_sum(a, b):
#     print("Сумма: ", end='')
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)


# #
# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))


# # Задание
#
# def maximum (one, two):
#     if one > two:
#         return one - two
#     else:
#         return one + two
#
#
# print(maximum(17, 16))


# # Задание
# #
# def cube(a):
#     return a ** 3 # a * a * a
#
#
# for i in range(1, 11): # Если переменная, то (1, 10 + 1)
#     print(i, "в кубе =", cube(i))

# # 2 вариант,  1 вариант лучше
# #
# def cube(a):
#     str = ''
#     for i in range(0, a + 1):
#         str += f'{i} в кубе = {i ** 3}\n'
#     return str
#
#
# res = cube(10)
# print(res)


# Задание, РАЗОБРАТЬСЯ
#
# def change(lst):
#     print(lst)
#     symbol1 = lst.pop(0)
#     sumbol2 = lst.pop()
#     lst.append(symbol1)
#     lst.insert(0, sumbol2)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# # 2 вариант (более проще)
# #
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#
#     return lst
#
#
# x = [1, 2, 3]
# result = change(x)
# print(result)
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# # Применение True и False вместо x и y в return
# #
# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = 10
# b = 15
# print(is_greater(a, b))
# print(is_greater(5, 10))
#
# if is_greater(a, b):
#     print(a, 'Больше', b)
# else:
#     print(b, 'Больше', a)


# # Проверка пароля РАСМОТРЕТЬ
# #
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это не надежный пароль")
