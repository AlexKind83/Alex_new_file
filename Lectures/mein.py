# name = "Alex"  # Инициализация переменной
# print("Hello,", name)
# age = 20
# print(age)
# text = "Hello"
# print(text)
# print(text + " " + str(age))
# print(type(age))  # int - целое число, float - число с плавающей точкой
# print(type(text))  # str - любое строковое значение
# a = True  # False
# print(a)  # bool - True, False - пишутся в верхнем регистре
# print(type(a))

# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))


# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)

# name_new = "Alex"

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # c = a
# # a = b
# # b = c
# a, b = b, a
# print("a:", a)
# print("b:", b)


# print("строка \
# символов")
# print('строка \n символов')
# print('строка \n'
#       'символов')
# print('\t строка \n    символов D:\\folder\\file.txt')


# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s1 + ", " + s2)
# print(s1 + ",     " + s2)
# # print(s1, ", ",  s2, "!")
# b = (s3 * 5)
# print(b)


# print(194809578476545960694606596695086579)
# print(1.94809578476545960694606596695086579) # После точки выводит 15 символов 16 округляет


# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0
# print(6 / 4)  # 1.5
# print(6 // 2)  # 3
# print(6 / 4)  # 1.5
# print(6 // 4)  # 1
# print(6 ** 2)
# print(6 % 4)


# Урок 2


# num1 = 4321
# print("Исходное число:", num1)
# a = num1 / 10
# num1 //= 10
# b = num1 % 10
# num1 //= 100
# print(a)
# print(b)

# num1 = 4325
# print("Исходное число", num1)
# res = num1 % 10 * 1000
# num1 //= 10
# res += num1 % 10 * 100
# num1 //= 10
# res = num1 % 10 * 10
# num1 //= 10
# res += num1 % 10
# print(res)


# num1 = "2"
# num2 = 3
# # res = num1 + str(num2)
# res = int(num1) + num2
# print(res)


# print(int(3.8))
# print(round(3.543))
# print(type(round(3.543)))
# print(round(3.543, 2))
# print(type(round(3.543, 2)))
# print(round(3.595, 2))
# print(type(round(3.595, 2)))


# num1 = "2.3"
# num2 = 3
# # res = num1 + str(num2)
# res = float(num1) + num2
# res = round(res)
# print(res)


# name = "Виктория"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="---")
# print("Меня зовут", name + ". Мне", age, "лет.", sep=" ", end=" ")
# print("Я учу Python.")
# print("Меня зовут", name + ". Мне", age, "лет.", sep=" ", end="\n\n")
# print("Я учу Python.")
# print("Меня зовут", name + ". Мне", age, "лет.", sep=" ", end="--//--")
# print("Я учу Python.")


# name = input("Введите имя: ")
# print(name)


# num = input("Введите число: ")
# # print(num)
# # print(type(num))
# power = input("Введите степень: ")
# res = int(num) ** int(power)
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))

# num = input("Введите число: ")
# power = input("Введите степень: ")
# num = int(num)
# res = int(num) ** int(power)
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))


# # Не явное преобразование типов
# b1 = True
# b2 = False
# print(b1 + 5)  # 1 +5
# print(b2 + 5)  # 0 + 5

# False => "", 0, False, None

# print(bool("python"))
# print(bool(""))
# print(bool(-0.2))
# print(bool(0))
# print(bool(False))
# print(bool(None))
# test = None
# print(test)


# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 7)
# print(8 > 5)
# print(8 < 5)
# print(9 >= 9)
# print("привет" > "ПРИВЕТ")


# print(2 < 4 < 9)  # 2 < 4 < 9 => True && True => True
# print(2 * 5 > 7 >= 4 + 5)  # True && True => True
# print(3 * 5 <= 7 >= 2)  # False && True => False


# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False


# and означает и
# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False:True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False:False)


# # or означает или
# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True:False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False:True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False:False)


# # not означает не
# print(9 - 7)
# print(not 9 - 7)
# print(not 7 - 7)


# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)
#
# cnt1 = 5    # Может быть такой код (но он не приветствуется)
# if cnt1 < 10: cnt1 += 2; print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")


# side1 = int(input("Введите сторону 1: "))
# side2 = int(input("Введите сторону 2: "))
# side3 = int(input("Введите сторону 3: "))
# if user1 == user2 == user3:
#     print("Треугольник равносторонний")
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник равнобедренный")


#              # Как упростить код ввода диапазона

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ")
# elif day == 6 or day == 7:
#     print("Выходной день - ")
# else:
#     print("Такого дня недели не существует")

#           # 2 вариант
#           # расписывает каждый день

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# урок 3


# n = int(input('Введите количество ворон: '))
# if 0 <= n <= 9:
#     print('На ветке', n, end=' ')  # pass  # или 3 точки ... # чтобы не выдавалась ошибка
#     if n == 1:
#         print('ворона')
#     elif 2 <= n <= 4:  # n == 2 or n == 3 or n == 4
#         print('ворон')
#     else:
#         print('ворон')
# else:
#     print('Ошибка ввода данных')


# Аналог Конструкций switch JS (пока еще работает медленно)

# password = 'admin'

# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case _:  #
#         print('Логин не найден')


# Рассмотрение написание (| и case _)

# day = 'вторник'
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница':
#         print('Рабочий день')
#     case 'суббота' | 'воскресенье':
#         print('Выходной день')
#     case _:
#         print('Такого дня недели не существует')


# day = 'вторник'
# time = 15  # Рабочее время
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 11 or 13 <= 16:
#         print('Рабочий день')
#     case 'суббота' | 'воскресенье':
#         print('Выходной день')
#     case _:
#         print('Такого дня недели не существует')


# Термальное выражение

# a, b, = 10, 20
#
# print(a if a < b else b)  # Заменяет действие ниже
#
# # if a < b:
# #     print(a)
# # else:
# #     print(b)


# a, b, = 10, 20
#
# print('a == b' if a == b else 'a > b' if a > b else 'b > a')


# Задача делить на нуль нельзя

# a = 5
# b = 0
# print('На ноль делить нельзя ' if b == 0 else a / b)
# print(a / b)

# # 2 Вариант
# a = int(input('Введите числитель: '))
# b = int(input('Введите знаменатель: '))
# print('Результат: ', a / b if b else 'На ноль делить нельзя')


# # Если пользователь ввел число вместо цифры
#
# try:
#     n = int(input('Введите целое число: '))
#     print(n * 2)
# except ValueError:  # чтобы не подчеркивалось except нужно указать имя ошибки
#     print('Что-то пошло не так')
#
# print('Следующая строка')


# Если пользователь ввел число вместо цифры, или делил на ноль

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except ValueError:
#     print('Нельзя вводить строки')
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')

# # 2 вариант
# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('Нельзя вводить строки или нельзя делить на ноль')
# else:  # когда в блоке try не возникло исключение
#     print('Все нормально. Вы ввели числа', n, 'и', m)
# finally:  # выполнится в любом случае
#     print('Конец программы')


# # Задача
# n = (input('Введите первое число: '))
# m = (input('Введите второе число: '))
#
# try:
#     n = int(n)  # n = 5
#     m = int(m)  # m = 'два'
# except ValueError:
#     n = str(n)  # n = 5
# finally:
#     print(n + m)  # '5' + 'два'


# Циклы # Итерация это 1 шаг цикла
# while # нет ++i только i += 1

# i = 0
# while i < 5:
#     print('i =', i)
#     i = i + 1  # i += 1

# i = 10
# while i > 0:
#     print('i =', i)
#     i -= 1


# Задача
# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# # 2
# i = 2
# while i <= 20:
#     print("i =", i)
#     i += 2


# Задача

# n = int(input('Кол-во символов: '))
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1

# 2 вариант
# n = int(input('Кол-во символов: '))
# print('*' * n)

# 3
# n = int(input('Кол-во символов: '))
# i = 0
# while i < n:
#     print('*')
#     i += 1
# print('*\n' * n)


# Задача

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# res = 0
# while a <= b:
#     if a % 2 != 0:
#         res += a
#     a += 1
# print(res)

# 2
# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# if a % 2:
#     a += 1
# res = 0
# while a <= b:
#     res += a
#     a += 2
# print(res)


# 3 урок


# n = input('Введите целое число: ')
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input('Введите целое число: ')
#
# if n % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# 2
# n = input('Введите число: ')
#
# while type(n) != int and type(n) != float:
#     try:
#         n = int(n)
#     except ValueError:
#         try:
#             n = float(n)
#         except ValueError:
#             print("Число не целое и не вещественное!")
#             n = input('Введите число: ')
#
# if n % 2:
#     print('Четное')
# else:
#     print('Нечетное')


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\n Цикл завершен')


# # Выход из бесконечного цикла 1
# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# # Выход из бесконечного цикла 2
# while True:
#     n = int(input('Введите положительное число: '))
#     if n < 0:
#         break


# # Задание
# res = 0
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
#
# print(res)


# # else выведется
# i = 0
# while i < 10:
#     print(i, end='')
#     i += 1
# else:
#     print('\n Цикл окончен, i =', i)
#
# # 2 прерван цикл  и не выведется else
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i, end='')
#     i += 1
# else:
#     print('\n Цикл окончен, i =', i)


# # Вложенные циклы
# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\t Внутренний цикл: j =', j)
#         j += 1
#     i += 1
#
# #  2 Не выведется j больше 1 раза
# j = 1
# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#
#     while j < 4:
#         print('\t Внутренний цикл: j =', j)
#         j += 1
#     i += 1


# # Задача
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, end='\t\t')  # пропишется одной строкой
#         j += 1
#     print()  # каждый цикл i пропишется отдельной строкой
#     i += 1


# # Задача символы чередуются в каждой строке
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1


# Символы по диагонали
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(' ', end="")
#         j += 1
#     print('*')
#     i += 1

# 2 эта же задача в коротком варианте
# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1


# # Цикл  for element in collection
# #           print(element)


# # Цикл for проход по переменной
# for i in 'Hello':
#     print(i)
#
#
# # Цикл for проход по кортежу
# for i in 'Hello', 'World', '!':
#     print(i)


# # range (start, stop, step)
#
#
# # Используем Метод range()
# for i in range(9):
#     print(i, end=' ')

# 2 сравнение Метод range() с Циклов while
# i = 2
# while i < 9:
#     print(i, end=' ')
#     i += 2


# # Два примера на сравнения, используя Метод range(), и Цикл while
# a = 9
# for i in range(0, a + 1):
#     print(i, end=' ')
#
# print()

# i = 0
# while i <= 9:
#     print(i, end=' ')
#     i += 1


# # Задача # вывести все числа которые делятся без остатка
# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# # Вывести числа, где две цифры одинаковые
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')


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
# print(c)


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


#
s = [5, 9, 3, 7, 9, 1, 8, 9]
print(s)
num = s.count(9)  # считает кол-во заданных значений списка
# print(num)

# ind = s.index(9)  # возвращает индекс первого искомого элемента
# print(ind)
# ind = s.index(8, 5, -1)  # если такого индекса не существует, то выдает ошибку
# print(ind)

a = 9
if a in s:
    ind = s.index(a)
    print(ind)
else:
    print("Элемента")
