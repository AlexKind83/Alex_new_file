# Урок 18

# # Создаем генератор случайного пароля
# #
# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def randon_password():
#     random_length = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(random_length):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print(("Ваш случайный пароль:", randon_password()))


# # Методы
# #
# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # 1 символ в строке в верхнем регистре
# print(s.lower())  # Лаувер
# print((s.upper()))  #
# print(s.swapcase())  #
# print(s.title())  #
# print(s)
#
# s = "hello, WORLD! I am learning Python."
# print(s.count("h"))  # возвращает количество указанных элементов
# print(s.count('h', 1, 10))
#
# print(s.find('Python'))  # ищет в строке подстроку и возвращает ее индекс, если его нет то возвращает -1
# print(s.find('Python', 10, 20))
#
# print(s.find('l'))
# print(s.rfind('l'))
#
# print(s.index('l'))  # ищет в строке подстроку и возвращает ее индекс, если его нет то возвращает ошибку
# print(s.rindex('l'))


# # Задача
# #
# _s = input("Введите два слова через пробел: ")  # один два
# first = _s[:_s.find(' ')]
# second = _s[_s.find(' ') + 1:]
# print(first)
# print(second)
#
# print(second + ' ' + first)


# #
# #
# s = "hello, WORLD! I am learning Python."
#
# print((s.startswith('hello')))  # возвращает True, если строка начинается с указанной подстроки
#
# print(s.find('I am'))
# print(s.startswith('I am', 14))
#
# print(s.endswith('on.'))  # возвращает True, если строка заканчивается с указанной подстроки
# print(s.endswith('lo', 3))
# print(s.endswith('lo', 3, 5))
#
# print('abc123'.isalpha())  # (ис альфа)
# print('abcABC'.isalpha())  # определяет, состоит ли строка только из букв
# print(''.isalpha())
#
# print('123'.isdigit())  # определяет, состоит ли строка только из цифр
# print('123.234'.isdigit())
#
# print('abc123'.isalnum())  # определяет, состоит ли строка только из букв и цифр
# print('abcA123'.isalnum())
#
# print('abc'.islower())  # определяет, являются буквенные символы строки в нижнем регистре(прописные)
# print('!abc456'.islower())
#
# print('!456A'.isupper())  #
#
# print('py'.center(10, '-'))  # Выравнивает строку по центру (метод для форматирования)
# print('py'.center(11, '+'))
#
# print('       py'.lstrip())
# print('py       '.rstrip())
# print('    py    '.strip())
#
# print("https://www.python.org".lstrip())
# print("https://www.python.org".lstrip('/:pths'))
# print("https://www.pythons.org".lstrip('/:pths').rstrip('.org'))
# print("https://www.pythons.org".strip('/:pths.org'))
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1)
# print(str1.replace('Nython', 'Python', 2))
#
# s1 = '-'
# seq = ('a', 'b', 'c')
# print(s1.join(seq))  # объединение итерируемой последовательности (состоит из строковых значений) в строку
# print('..'.join(['1', '2']))
# print(':'.join('hello'))
#
# s = "hello, WORLD! I am learning Python."
# print(s.split())
# print('www.python.org'.split('.'))
# print('www.python.org'.split('.', 1))  # делит строку на список, состоящий из строк
# print('www.python.org'.rsplit('.', 2))


# # Задача (Рассмотреть и вспомнить обращение по индексу)
# #
# a = input('-> ').split()
# print(a)
# print(a[0], a[1][0] + '.' + a[2][0] + '.')


# # Используя метод строки split но на выходе приводим к int числовому значению (ЗАПОМНИТЬ)
# #
# a = input("Введите коды символов через пробел: ").split()
# print(a)
#
# b = list(map(int, a))
# print(b)
#
# # В одну строку
# a2 = list(map(int, input("Введите коды символов через пробел: ").split()))
# print(a2)


# Регулярные выражения
#
#
import re
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r'\w+'
# print(re.finditer(reg, s))  # возвращает список, содержащий все совпадения с, шаблонам
#
# print(re.search(reg, s))  # возвращает месторасположение первого совпадение с, шаблонам
# print(re.search(reg, s).span())  # (6, 16)
# print(re.search(reg, s).start())  # 6
# print(re.search(reg, s).end())  # 16
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = 'Я ищу'
# print(re.match(reg, s))  # возвращает месторасположение
# print(re.match(reg, s).start())
# print(re.match(reg, s).end())
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = '[.я2]'
# print(re.split(reg, s))  # Возвращает список, в котором строка разбита по шаблону
# print(re.split(reg, s, 1))
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r'\.'  # r спец символ (сырая строка) [нужен чтобы не надо было экранировать (\.)]
# print(re.sub(reg, '!', s))  # поиск и замена


# #
# #
# import re
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765"
# # reg = r"[12][0-9][0-9][0-9]"
# reg = r"[А-яЁё]"
# print(re.findall(reg, s))
#
# print(ord("Ё"))
# print(ord('А'))
#
# print(ord('я'))
# print(ord('я'))
#
# print(ord('ё'))






# Урок 19

# import re

# #
# #
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765 Hel_lo[-World]"
# reg = r'\w+'
# # reg = r'20*'  # 1 элемент обязателен (2 едет только после 1 элемента)
#
#
# print(re.findall(reg, s))


# Задача
#
# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15Е21:59. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# req = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(req, st))


#
#
# d = "Цифры: 7б +17, -42, 0013, 0.3"
# print(re.findall(r'[+-]?\d+[.\d]*', d))


# # Поиск и замена регулярного выражения РАСМОТРЕТЬ ОБЯЗАТЕЛЬНО
# #
# st = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub('-', '.', re.sub(r'#.+', '', st)))
# print("Дата рождения:", re.sub(r'\s#.*', '', st).replace('-', '.'))
# print('Дата рождения:', re.sub(r'-', '.', re.search(r'\d{2}-\d{2}-\d{4}', st).group()))


# # Задача
# #
# st = 'author=Пушкин А. С.; title = Евгений Онегин; price =200; year= 1831'
# # reg = r'\w+\s*=\s*\w+'  # плохой подход
# reg = r'[^;]+'
# print(re.findall(reg, st))


# #
# #
# st = "12 сентября 2021 года 2356858475609"
# reg1 = r'\d{2,4}'
# reg2 = r'\d{2,}'
# reg3 = r'\d{,4}'
#
# print(re.findall(reg1, st))
# print(re.findall(reg2, st))
# print(re.findall(reg3, st))


# # Задача
# #
# st = '+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, st))


# #
# #
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765 Hel_lo[-World] 2875438 6968345"
# # reg = r'\w+\s\w+'
# # reg = r'^\w+\s\w+'
# # reg = r'\w+\s\w+$'
#
# print(re.findall(reg, s))  # findall (файнтбол)


# # Функция с шаблоном регулярного выражения
# #
# def valid_login(name):
#     return re.findall(r'^[A-Za-z0-9_-]{6,16}$', name)  # 6-16, англ. буквы, _, -, [0-9]
#
#
# print(valid_login("Python_master"))
# print(valid_login("!!!!Python"))
# print(valid_login("Python!!!!"))
# print(valid_login("Python!!!Python"))


# # Флаги шаблона регулярного выражения
# # РАСМОТРЕТЬ ВНИМАТЕЛЬНО
# #
# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))
# print(re.findall(r'\w+', '12 + й', flags=re.A))
# print(re.findall(r'\w+', '12 + й', re.A))


# text = "hello world"
# # print(re.findall(r'\w+', text))
# print(re.findall(r'\w+', text, re.DEBUG))
# print(re.findall(r'\w\+', text, re.DEBUG))


# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r'я'
# print(re.findall(reg, s, re.IGNORECASE))


# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text))  # one\ntwo
# print(re.findall(r'one.\w+', text, re.DOTALL))  # one\ntwo

# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))


# print(re.findall(r"""
# [a-z.-]+    # part 1
# @           # @
# [a-z.-]+    # part 2
# """, 'test@mail.ru', re.VERBOSE))  # Если нужен комментарий, пробел, или перенос на другую строку


# # Используем многого флагов в многострочном тексте
# #
# text = """Python
# python
# PYTHON"""
# reg = r'(?im)^python'
# print(re.findall(reg, text))
