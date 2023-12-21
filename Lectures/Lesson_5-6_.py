# Урок 5


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')


# for i in range(3):
#     print("+++", i)
#     for j in range(2):
#         print("----- j =", j)


# # Длина и высота символов
#
# w = 16
# h = 4
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()


# # Задача: Вывести прямоугольник где внутри его пустота
#
# w = int(input("Введите ширину прямоугольника: ")) # 16
# h = int(input("Введите высоту прямоугольника: ")) # 4
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# # Массив с использованием for (произойдет цикл range)
# # УДЕЛИТЬ ВНИМАНИЕ
# #
# # nums = [letter * 2 for letter in "Banana"] # 1 пример
# nums = [i for i in range(30) if i % 2 == 0] # 2 пример
# print(nums)


# # Список (list)
# #
# #
# nums = [8, 3, 9, 4, 1, "one"]
# print(nums)
# print(type(nums))
#
# print(nums[0])
# print(nums[2])
# # print(nums[6]) # IndexError
# print(nums[-1])
# print(nums[-2])
#
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)


# # Чтобы посчитать длину списка надо к range добавить длину len и саму переменную nums
# #
# nums = [8, 3, 9, 4, 1]
# # print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] ** 2) # Обратиться не к индексу, а значению списка


# s = []
# print(s)
#
# b = list("Hello")
# print(b)


# #
# print(range(6))
# n = list(range(6))
# print(n)
#
# print(list(range(2, 10)))
# print(list(range(2, 10, 2)))
# print(list(range(2, 10 + 1, 2)))


# #
# # [выражение for переменная in последовательность] -- генератор for
# #
# #
# a = [0 for _ in range(5)] # a = [0 for i in range(5)]
# print(a)
# b = [i for i in range(5)]
# print(b)


# #
# n = 5
# b = [i ** 2 for i in range(1, n + 1)] # Если хотим чтобы цикл начинался не с )
# print(b)


# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)


# # Перезапись списка с помощью range, с использованием стрелки в input
# #
# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)


# # Пример выше только используется генератор for
# #
# a = [input("-> ") for i in range(int(input("n = ")))]
# print(a)


# # Задача
# # Посчитать в списке сумму всех отрицательных элементов
# #
# a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма: ", s)

# # 2 решение задачи с использованием sum()
#
# a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# print("Сумма отрицательных элементов: ", sum([num for num in a if num < 0]))


# # 2 Варианта пробежки по строке:
# #
# a = list(range(10, 100, 10))
# print(a)
#
# # 1 Вариант (Получаем значение по индексу)
# for i in range(len(a)): # 0 1 2 3 4 5 6 7 8
#     print(a[i] + 2, end=" ") # a[i] = 10 20 30 40 50 60 70 80 09
# print()
#
# # 2 Вариант (Получаем значение без индекса)
# for i in a:
#     print(i + 2, end=" ") # 10 20 30 40 50 60 70 80 90


# # Задача
# # 1 решение
#
# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
#
# print("Количество четных элементов: ", k)
# print("Сумма нечетных элементов: ", s)

# # 2 решение
#
# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("Количество четных элементов: ", k)
# print("Сумма нечетных элементов: ", s)
#


# Задача, где второй пример который выше не сработает правильно.
# Выведите все элементы списка которые больше предыдущего.
# Как находить элемент который больше или меньше пре ведущего.
#
# n = list(range(21, 41, 2))
# print(n)
# a = 2
# print(n[a])
# print(n[a-1])
# print(n[a+1])

# a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# for i in range(1, len(a)):
#     # print(a[i], '-> ', end='')
#     # print(a[i - 1])
#     if a[i] > a[i - 1]: # больше пре ведущего элемента.
#         print(a[i], end=' ')




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


# # Задание, создать срезы изи списка
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

# # 2 Вариант
# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7, 2, 4]
# c = []
#
# for element in a:
#     if element in c and element not in b:
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
