# Этих 3 команд достаточно, чтобы добавить в репозиторий удаленные файлы.

# 1) gid add .
# 2) git commit -m "added print"
# 3) git push


#
# git clone ссылка для скопированная

# git pull
# -- Забираем изменения с удаленного репозитория в локальный
# забираем данные с удаленного репозитория(с другого компа папки и т.п.)

#

#


# Урок 11

#
# Множество (set) (Хранит только уникальные данные -- без повторений)
#

# s = {'banana', 'apple', 'orange', 'banana', 'apple'}
# print(s)
# print(type(s))
# print(len(s))


# # Создаем класс set
# #
# a = set()
# print(a, type(a))
#
# c = ['red', 'blue', 'green', 'red']
# b = set(c)
# print(b, type(b))


#
#
# mas = [1, 2, 3, 2, 3, 4, 4, 5]
# s = {x for x in mas if x % 2 == 0} # Можно не только сгенерировать, но и применить if
# print(s)


# # Задача
# #
# def to_set(elem):
#     st = set(elem)
#     return st, len(st)
#
#
# print(to_set("я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# # Не у, порядочный цикл
# #
# t = {'red', 'green', 'blue'}
# # print('green' not in t)
# for i in t:
#     print(i)


# # Где нужен if и else одновременно (термальное выражение), записывается в левой стороне
# # РАСМОТРЕТЬ
# #
# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = [i for i in r if 'a' not in i]
# b = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# c = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)
# print(b)
# print(c)


# # Методы множества (посмотреть документ множеств)
# #
# a = {'Tom', 'Bob', 'Alice'}
# print(a)
#
# a.add('Ann')
# print(a)
#
# a.remove('Ann')
# print(a)
#
# user = 'Tom' # Если данных нет, то произойдет ошибка, в таких случаях надо делать проверку
# if user in a:
#     a.remove(user)
# print(a)
#
# a.discard('Ann') # Есть или нет этого элемента, удалит если нет то не удалит(проверка не нужна)
# print(a)
#
# n = a.pop() # Удаляет Первый элемент, и возвращает
# print(n)
# print(a)
#
# a.clear()
# print(a)


# Методы и операторы (для сокращения методов)
#
# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}

# # c = a.union(b)
# c = a | b # Добавляем в --c
# a |= b # Добавляем в --a
# print(c)
# print(a)

# c = a & b
# a &= b
# print(c)
# print(a)

# c = a - b
# a -= b
# print(c)
# print(a)

# c = a ^ b
# a ^= b
# print(c)
# print(a)


# # Задача
# #
# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7) # итерируемые -- это через запятую
# # print(s)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
#
# count = len(s)
# print('Count:', count)
# print('Min:', min(s))
# print('Max:', max(s))
# print('Sum:', sum(s))


# Задача (Строки надо переводить в set)
#
# 1
#
# s1 = 'Hello'
# s2 = "How are you"
#
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=' ')

# # 2
#
# s1 = set('Hello')
# s2 = set("How are you")
#
# a = s1 & s2
# print(a)
# for i in a:
#     print(i, end=' ')


# # Задача
# #
# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# one_hobby = drawing ^ music
# print("Один кружок: ", one_hobby)
#
# both_hobbies = drawing & music
# print("Оба кружка: ", both_hobbies)
#
# # drawing = drawing - both_hobbies
# drawing -= both_hobbies
# print("Кружок рисования: ", drawing)


#
# #
# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)


# #
# # Тип frozenset (Замороженный set, не изменяемый set)
# # Только работают операторы с этим типом данных
# #
# s = frozenset()
# s1 = frozenset([1, 2, 3, 4, 5])
# print(s1, type(s))
# a = frozenset({'Hello', 'World'})
# print(a)


# # Изменения типа данных set в list и обратно
# #
# a = [0, 9, 7, 4, 5, 8, 7, 9, 4, 6, 5, 1, 2, 3, 5]
# print(a)
# b = set(a)
# print(b)
# a = list(b)
# print(a)






# Урок 12


#
#
# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3, 4: 'four'}
# lst[0] = 10
# print(lst[0])
# d['one'] = 10
# print(d['one'])
# print((d[4]))


# #
# # Создание словарей
# #
# d = {'one': 1, 'two': 2}
# print(d, type(d))
#
# d1 = dict({'one': 1, 'two': 2})
# print(d1, type(d1))
#
# d2 = dict(one=1, two=2, four='four') # Так словари создавать не рекомендуется
# print(d2, type(d2))


# # Любой не изменяемый тип данных может быть Ключом (Значение может быть все что угодно!)
# # При перезаписи словаря, ключи одинаковые записываются первыми, а значение последние!
# # При записи ключа True == 1, False == 0.
# #
# d3 = {0: 1, 'two': 2, (1, 2.3): 'кортеж', True: [2, 3, 6, 7], 1: 45, False: (1, 2)}
# print(d3)


# # Обращаемся к индексу элементов словаря
# #
# d = {0: 1, 'two': 2, (1, 2.3): 'кортеж', True: [2, 3, 6, 7]}
# print(d)
# print((d[True][1]))
# print(d[(1, 2.3)])
# print(d['two'])
# print(d[0])


# # Два значения мы можем преобразовать в словарь
# #
# lst = (('one', 1), ('two', 2), ('three', 3))
# d = dict(lst)
# print(d)


# # Генератор словаря
# #
# d = {a: a ** 2 for a in range(7)}
# print(d)


# Проверки на если вдруг есть не существующий ключ
#
# d = {'one': 1, 'two': 2, 'four': 4}
# key = 'four1'

# if key in d:
#     del d[key]

# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + " нет в словаре")
#
# for i in d:
#     print(i, '->', d[i])


# # Задача
# #
# myDict = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# composition = 1
# for key in myDict:
#     composition *= myDict[key]
# print('Произведение:', composition)
#
# # 2 решение
# numbers = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
#
# result = 1
# for value in numbers.values():
#     result *= value
#
# print(result)


# # Задача
# #
# # d[1] = input('-> ')
# # d[2] = input('-> ')
# # d[3] = input('-> ')
# # d[4] = input('-> ')
#
# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)


# #
# #
# myDict = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(len(myDict))
# print(min(myDict))
# myDict = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(sum(myDict))


# # Задача РАСМОТРЕТЬ
# #
# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670k', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400],
# }
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')

# while True:
#     n = input('№: ') # '2'
#     if n != '0':
#         gty = int(input('Количество: ')) # 8
#         try:
#             goods[n][1] += gty
#         except KeyError:
#             pass
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')


# #
# # Методы словарей (полезные методы) Сами по себе бесполезны, лучшее применение в цикле
# #
#
# d = {'a': 1, 'b': 2, 'c': 3}
#
# print(d.keys()) # список ключей
# print(d.values()) # список значений
# print(d.items()) # Список ключей и значений
#
# for i in d.keys():
#     print(i)
#
# for i in d.items():
#     print(i)
#
# for i, j in d.items():
#     print(i, '->', j)
#
# print(list(d))
# print(list(d.keys()))
# print(list(d.items()))
#
# print(tuple(d))
# print(list(d.keys()))
# print(list(d.items()))


#
# #
# d = {'a': 1, 'b': 2, 'c': 3}
#
# d2 = d.copy()
#
# print('d:', d, id(d))
# print('d2:', d2, id(d2))
#
# d2['a'] = 5
# d['e'] = 7
#
# print('d:', d, id(d))
# print('d2:', d2, id(d2))
#
# d.clear() # Очищает словарь
#
# print('d:', d, id(d))
# print('d2:', d2, id(d2))


#
# Редко используемые методы dict
#
# d = {'a': 1, 'b': 2, 'c': 3}


# print(d['b'])
# value = d.get('e', "Такого ключа не существует") # Если ключа нет возвращается второй параметр или None
# print(value)

# item = d.pop('e', "Такого ключа нет") # Удаляет значение по ключу, если такого ключа нет, то возвращает 2 пар.
# print(item)
# print(d)

# item = d.popitem() # Удаляет последний созданный элемент, и возвращает элемент
# print(item)
# print(d)
