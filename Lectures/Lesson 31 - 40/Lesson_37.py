""""""
import csv

# Урок 37

# pip install lxml (Рекомендуемый)
# Записать(видео)
#

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r'\D+', '', s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a', encoding='UTF-8') as fa:
#         writer = csv.writer(fa, delimiter=';', lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['rating']))
#         #  Можно не в кортеж передавать, а в список, только в списке будем использовать индекс
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     s = soup.find_all('section', class_='plugin-section')[1]
#     plugins = s.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         url = plugin.find('h3').find('a').get('href')  # 1 способ получения .get('href')
#         # rating = plugin.find('span', class_='rating-count').text  # Получаем с круглыми скобками
#         rating = plugin.find('span', class_='rating-count').find('a').text  # Убираем круглые скобки
#         r = refined(rating)  # Убираем лишние (буквы в рейтинге)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# # Записать (видео) и сделать коммент что делаем
# #
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins1.csv', 'a', encoding='UTF-8') as fa:
#         writer = csv.writer(fa, delimiter=';', lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active'], data['test_version']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all('article')
#     for element in elements:
#         try:
#             name = element.find('h3').text
#         except AttributeError:
#             name = ''
#
#         try:
#             url = element.find('h3').find('a')['href']  # 2 вариант вместо .get('href')
#         except AttributeError:
#             url = ''
#
#         try:
#             snippet = element.find('div', class_='entry-excerpt').text.strip()  # Убираем пробелы
#         except AttributeError:
#             snippet = ''
#
#         try:
#             active = element.find('span', class_='active-installs').text.strip()  # Убираем пробелы
#         except AttributeError:
#             active = ''
#
#         try:
#             test_version_1 = element.find('span', class_='tested-with').text.strip()
#             test_version_2 = refine_cy(test_version_1)
#         except AttributeError:
#             test_version_2 = ''
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'test_version': test_version_2,
#         }
#
#         write_csv(data)
#
#
# def main():
#     for i in range(1, 25):
#         url = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}/'
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


#
#

from Parser_37 import Parser


def Lesson_37():
    pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
    pars.run()


if __name__ == '__main__':
    Lesson_37()
