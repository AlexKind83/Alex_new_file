""""""

import csv
import requests
import json

# Урок 36

"""Формат  CSV = Переменные разделенные запятыми"""  # Продолжаем

# with open('data.csv', encoding='UTF-8') as f:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']}")
#         count += 1


# Убираем пустоту между новыми строками
#
# with open('student.csv', 'w', encoding='UTF-8') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # Убирает промежуток между новыми строками (lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', 9, 15])
#     writer.writerow(['Саша', 5, 12])
#     writer.writerow(['Маша', 11, 18])


# Список в списке
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_new.csv', 'w', encoding='UTF-8') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     for row in data:
#         writer.writerow(row)
#
# with open('data_new.csv') as f:
#     print(type(f.read()))
#     print(f.read())  # Если просто надо считать файл

# -------------------------------------------------------------

# writerows(data) - Заменяет цикл

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_new.csv', 'w', encoding='UTF-8') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerows(data)  # помогает работать список-в списке (заменяет цикл)
#
# with open('data_new.csv') as f:
#     print(type(f.read()))
#     print(f.read())  # Если просто надо считать файл


# writeheader() - записывает список словарей
#
# with open('stud.csv', 'w', encoding='UTF-8') as f:
#     names = ['Имя', 'Возраст']
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     writer.writeheader()
#     writer.writerow({'Имя': 'Саша', 'Возраст': 6})
#     writer.writerow({'Имя': 'Маша', 'Возраст': 15})
#     writer.writerow({'Имя': 'Вова', 'Возраст': 14})


#
#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
#
# with open('dict_writer.csv', 'w', encoding='UTF-8') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(data[0].keys()))
#     # list(data[0].keys() = list иногда необходим но не всегда
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)
#
# # print(data[0].keys())  # 1 вариант получения, что содержится
# # print(list(data[0].keys()))  # 2 вариант получения, что содержится


# # Получаем данные из json и записываем в csv
# #
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# with open('todos.csv', 'w', encoding='UTF-8') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(todos[0].keys()))
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)


"""Парсинг"""
# pip install beautifulsoup4 или bs4

from bs4 import BeautifulSoup
# Обязательно записать рассказ о парсинг

f = open('index.html').read()
# print(type(f))
# print(f)
soup = BeautifulSoup(f, 'html.parser')

row = soup.find('div', class_='name')  # .text (покажет что в теге записано)
# Ищет по тегу значение атрибута (ищет 1 встретившийся Элемент)

# row = soup.find_all('div', class_='name')  # ищет все элементы тега

# row = soup.find_all('div', class_='row')[1].find('div', class_='links')
# # получаем из div row именно в нем div links

# row = soup.find_all('div', {'data-set': 'salary'})
# # Получаем по пользовательскому классу (надо создать условия как dict)

# row = soup.find_all('div', {'class': 'name'})
# другой синтаксис записи (row = soup.find_all('div', class_='name'))

# row = soup.find('div', string="Alena")
# row = soup.find('div', string="Alena").parent
# row = soup.find('div', string="Alena").parent.parent  # 1
# row = soup.find('div', string="Alena").find_parent(class_='row')  # 2
# Получаем доступы на уровень выше

# row = soup.find('div', id='whois3')
# С id обычно используется метод (find), в другом случай мы получим список (find_all)
# row = soup.find('div', id='whois3').find_next_sibling()  # Получаем следующий элемент на этом уровне
# row = soup.find('div', id='whois3').find_previous_sibling()  # Получаем при ведущий элемент на этом уровне

# -------------------------------------------------------------------------

# Получить данные по определенному условию(ищем именно конкретную профессию (Copywriter))
# Желательно записать видео


# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois').text
#     # print(whois)
#     if 'Copywriter' in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding='UTF-8').read()
# soup = BeautifulSoup(f, 'html.parser')
#
# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)


# # # Ищем все зарплаты.
# # # Записать видео
# #
# import re
#
#
# def get_salary(s):
#     pattern = r'\d+'
#     # res = re.findall(pattern, s)[0]  # 1
#     res = re.search(pattern, s).group()  # 2
#     print(res)
#
#
# f = open('index.html', encoding='UTF-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})
#
# for i in salary:
#     get_salary(i.text)


#
# Тоже записать видео

# r = requests.get('https://ru.wordpress.org/')
# print(r)
# print(r.status_code)

# print(r.headers)
# print(r.headers['Content-Type'])

# print(r.content)  # Получили и за Русского языка данные в бинарном формате
# print(r.text)  # Получили текстовую содержимое у модуля requests (читабельное)


# #
# # И это под запись (а то в будущем сложно будет востановить событие исполняемости)
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    p1 = soup.find('header', id='masthead').find('p', class_='site-title').text
    return p1

# r = requests.get('https://ru.wordpress.org/')
# print(r.text)


def main():
    url = 'https://ru.wordpress.org/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()

