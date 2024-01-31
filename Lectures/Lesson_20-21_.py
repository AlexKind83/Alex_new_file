# Урок 20
# import re


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))


# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r'<img.*?>'
# # reg = r'<img[^>]*>'
# print(re.findall(reg, s))


# s = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))


# # Задача
# #
# text = ("Python (в русском языке встречаются названия пито́н[16]или "
#         "па́йтон[17]) — высокоуровневый язык "
#         "программирования общего назначения с динамической строгой типизацией "
#         "и автоматическим управлением памятью[18][19].")
#
# my_reg_1 = r'\[.*?\]'
# my_reg_2 = r'\[[^\]]*\]'  # вариант менее красив в данном случай
# # reg = r"\[\d+\]"  # Самый красивый вариант
# # print(re.findall(reg, text))
# print(re.findall(my_reg_1, text))
# print(re.findall(my_reg_2, text))


# # (?:...) - это группирующая скобка является не сохраняющей ВНИМАНИЕ
# #
# s = 'int = 4, float = 4.0f, double = 8.0'
# # reg = r'\w+\s*=\s*\d[.\w]*'
# # reg = r'int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*'
# reg = r'(?:int|float)\s*=\s*\d[.\w]*'
# print(re.findall(reg, s))


# # (?:...){3} - повторяет что в круглых скобках
# #
# s = '127.168.257.255'
# # reg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.'
# reg = r'(?:\d{1,3}\.){3}\d{1,3}'
#
# print(re.findall(reg, s))
# # print(re.search(reg, s).group())


# # В re-функций split - (круглые скобки помогают включить эти символы в массив, и ИСКЛЮЧИТЬ пробельные символы!)
# #
# s = '5 + 7*2 - 4'
# reg = r'\s*([*+-])\s*'
# print(re.split(reg, s))


# # Задача (Используем или |)
# #
# s = '01-08-2021'
# pattern = r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(pattern, s))
# print(re.search(pattern, s).group())


# # Ищем по индексу Match-объекты (это возможно только с помощью группы)
# #
# s = "Я ищу совпадения в 2024 году. И я их наиду в 2 счета."
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s).group(1))
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])


# #
# #
# text = """
# Самара
# Москва
# Тверь
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# # (?P(name>...) - даем имя группе
# # Работа с кавычками
# #
# s = "<p>Изображение <img alt='картинка' src=\"bg.jpg\"> - фон страницы</p>"
# # reg = r"<img\s+[^>]*src\s*=(['\"])(.+?)\1>"
# reg = r"<img\s+[^>]*src\s*=(?P<name>['\"])(.+?)\1>"
# print(re.findall(reg, s))


# # Меняем группы местами (можем это сделать только в заменяемом параметре) в re-функций sub
# #
# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024."  # 23.10.2024
# reg = '(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))


# # РАСМОТРЕТЬ И ЗАПИСАТЬ
# #
# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s, re.IGNORECASE))






#  Урок 21

#
# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input("На каком Вы этаже: "))  # 5
# elevator(n1)


# # 2 Примера (1 - без рекурсий) (2 - с рекурсией)
# #
# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 2, 3, 4, 5]))
#
# # Теперь пример Рекурсий
#
#
# def sum_list(lst):
#     if len(lst) == 1:
#         return lst
#     else:
#         print(lst)
#         return lst + sum_list(lst[1:])
#
#
# print(sum_list([1, 2, 3, 4, 5]))


# # Случай где базовым циклом нельзя выполнить (только рекурсией)
# #
# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         # возвращаются данные из стека
#         return convert[n]
#     else:
#         # в, вызываемой функций происходит вычисление, и приходят новые параметры в начало функций
#         # из convert[по индексу] получаем данные которые сохраняются в стек
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(365, 10))
# print(to_str(18, 2))
# print(to_str(18,8))
# print(to_str(18, 16))


# # Функция isinstance()
# # проверяем является или нет Списком
#
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))


# # # Подсчитываем сколько элементов на всех уровнях вложенности
# # #
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(names)
#
#
# def count_item(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print((count_item(names)))


# # Убираем табуляцию и пробел из строки
# #
# def remove(text):
#     if not text:
#         return ""
#     if text[0] == '\t' or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\tWorld "))


# Файлы
#

# Текстовые
# Бинарные

# # Открываем файлы
# #
# f = open(r'test2.txt', 'r')  # Относительный путь
# f2 = open(r'C:\Users\RobotComp.ru\Desktop\Новая папка\Python учеба\Lectures\test2.txt', 'r')  # Абсалютный путь
# print(*f)  # Чтение содержимого файла
# print(f)
# print(f.closed)  # Проверка закрыт или не закрыт файл
# f.close()
# print(f.closed)  # Проверка закрыт или не закрыт файл
# print(f.mode)
# print(f.name)
# print(f.encoding)


#
#
# f = open(r'test2.txt', 'r')
# print(f.read(3))  # Читает файл 3 символа
# print(f.read())  # Дочитывает файл или читает его полностью
# f.close()

# f = open('test1.txt', 'r')
# print(f.readline())  # считывает одну строку из файла
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('test1.txt', 'r')
# print(f.readlines(16))  # считал все данные из файла и вернул список из строк
# print(f.readline())
# f.close()

# f = open('test1.txt', 'r')
# for line in f:
#     print(line)
# f.close()


# # Задача
# #
# f = open('test1.txt', 'r')
# count = 0
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print('count =', count)
#
# f = open('test1.txt', 'r')
# print(len(f.readline()))
# f.close()


# Создаем файл и записываем в его данные
#
# f = open("xyz.txt", 'w')
# f.write("Hello\nWorld!\n")
# f.close()

# f = open("xyz.txt", 'a')
# f.write("New text.\n")
# f.close()

# f = open("xyz.txt", 'w')
# line = ["This is line 1\n", "This is line 2\n"]
# f.writelines(line)
# f.close()
