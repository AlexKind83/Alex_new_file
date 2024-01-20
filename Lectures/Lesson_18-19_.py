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
_s = input("Введите два слова через пробел: ")  # один два
first = _s[:_s.find(' ')]
second = _s[_s.find(' ') + 1:]
print(first)
print(second)

print(second + ' ' + first)


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
# print('py'.center(11, '-'))
#
# print('       py'.lstrip())
# print('py       '.rstrip())
# print('     py      '.strip())
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
# print('www.python.org'.split('.', 2))  # делит строку на список, состоящий из строк
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
# import re
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = 'совпадения'
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения с, шаблонам
#
# print(re.search(reg, s))  # возвращает месторасположение первого совпадение с, шаблонам
# print(re.search(reg, s).span())  # (6, 16)
# print(re.search(reg, s).start())  # 6
# print(re.search(reg, s).end())  # 16
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = 'ищу'
# print(re.match(reg, s))  # возвращает месторасположение ВНИМАНИЕ дописать
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = '[.я2]'
# print(re.split(reg, s))  # Возвращает список, в котором строка разбита по шаблону
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

