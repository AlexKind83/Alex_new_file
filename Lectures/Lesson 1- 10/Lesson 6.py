"""Срезы, список[start: stop: step], методы списка"""
# 6 урок


# # Срез
# # список[start: stop: step]
# a = [7, 8, 2, 1, 17, 9]
# print(a)
# # a[0], a[1] = a[1], a[0]
# # print(a)
# print(a[1:4])  # от элемента по индексу 1 до 4 не включая его
# print(a[1:])  # от 1 до конца списка
# print(a[:3])  # от начала списка до 3 не включая его
# print(a[::2])  # шаг 2,
# print(a[::-1])  # Развернули список
# print(a[5:2:-1])
#
# b = a[10:20]  # создаем пустой список с определенными индексами
# print(b)


# # Задание, создать срезы из списка
# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::-1])
# print(a[1::2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])


# # Срезы
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# s[2] = [20]
# s[3] = 20
# print(s)

# # s[2:5] = []  # Удаление без del
# del s[:]  # del функция удаления
# print(s)


# # Методы списков [добавляет]
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список нескольких элементов в конец списка
# print(s)
# s.extend('adc')
# print(s)
# s.insert(1, 100)  # добавляет элемент в заданный индекс
# print(s)
# s.insert(len(s), 220)  # добавит в конец
# s.insert(-1, 200)   # добавит в предпоследний
# print(s)

# print(dir(list))  # посмотреть список методов list


# # Добавляем элементы в начало и другим методом в конец
# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)


# Задача
# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     if x % 3 == 0:
#         s.append(x)
#         print(x)
#     else:
#         print("Число не кратное 3: ")
# print(s)


# # Если в первом и втором списке есть одинаковые числа, то выводятся
# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7,]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue  # повторяющей элементы списка (с) не повторяются
#         if i == j:
#             c.append(i)
#             break  # для того чтобы одинаковые числа больше не проверялись 2 список
# print(c)  # [2, 1, 4, 3]
#
# # 2 Вариант
# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7, 2, 4]
# c = []
#
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
#
# print(c)


# # Задача
# a = [1, 3, 5]
# b = [2, 4, 6]
# c = []
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
#
# print(c) # [1, 2, 3, 4, 5, 6]


#
# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b)):
#         c.append((b[i]))
#
# print(c)

# # 2 вариант когда список 1 длинней ([здесь не важно какой список длиннее])
# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33,]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append((b[i]))
# print(c)


# # Методы списков 2 [удаление]
# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# s.remove(9)  # удаляет элемент по заданному значению [один элемент]
# print(s)
# s.pop()  # без параметров - удалит последний элемент из списка
# a = s.pop(-1)  # передаем индекс для удаляемого элемента
# print(a)
# print(s)
# s.clear()  # очистка всех элементов
# print(s)


# Задача
# # a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# numbers = [6, 4, 7, 8, 9]
# index = int(input('Введите индекс удаляемого элемента: '))
# numbers.pop(index)
# print(numbers)


# #
# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# num = s.count(9)  # считает кол-во заданных значений списка
# # print(num)
#
# # ind = s.index(9)  # возвращает индекс первого искомого элемента
# # print(ind)
# # ind = s.index(8, 5, -1)  # если такого индекса не существует, то выдает ошибку
# # print(ind)
#
# a = 9
# if a in s:
#     ind = s.index(a)
#     print(ind)
# else:
#     print("Элемента")
