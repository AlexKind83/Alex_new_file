"""Содержит цикл for, range, список, генератор выражения \n
   генератор в генераторе, цикл в цикле. \n
   В if (continue, break), sum. \n
   Обращение по индексу списка."""
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


# Длина и высота символов

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
# b = [i ** 2 for i in range(1, n + 1)]  # Если хотим чтобы цикл длился (не включая 5, а до 5)
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

a = [int(input('-> ')) for _ in range(int(input('n = ')))]
for i in range(1, len(a)):
    # print(a[i], '-> ', end='')
    # print(a[i - 1])
    if a[i] > a[i - 1]:  # больше при ведущего элемента.
        print(a[i], end=' ')
