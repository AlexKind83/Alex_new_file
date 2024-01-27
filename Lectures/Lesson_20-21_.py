# Урок 20
import re

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))


# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img[^>]*>'
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
# reg = r"\[\d+\]"
# print(re.findall(reg, text))


# # (?:...) - это группирующая скобка является не сохраняющей ВНИМАНИЕ
# #
# s = 'int = 4, float = 4.0f, double = 8.0'
# # reg = r'\w+\s*=\s*\d[.\w]*'
# # reg = r'int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*'
# reg = r'(?:int|float)\s*=\s*\d[.\w]*'
# print(re.findall(reg, s))


# # (?:...){3} - повторяет что в круглых скобках
# #
# s = '127.168.255.255'
# # reg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.'
# reg = r'(?:\d{1,3}\.){3}\d{1,3}'
#
# print(re.findall(reg, s))
# print(re.search(reg, s).group())


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


