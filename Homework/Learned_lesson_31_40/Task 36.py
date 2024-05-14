"""Тренировочный парсинг"""
import requests
from bs4 import BeautifulSoup


def practice_html_1(url_1):
    """Получаем доступ по url адресу и возвращает его в def main()"""
    r = requests.get(url_1)
    return r.text


def practice_html_2(url_2):
    """Получаем доступ по url адресу и возвращает его в def main()"""
    r = requests.get(url_2)
    return r.text


def get_data_1(html):
    """Парсинг страницы"""
    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.find('div', id="recent-posts-2").find_all('li')[1].text
    return datas


def get_data_2(html):
    """Парсинг страницы"""
    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.find('div', class_="table-of-contents__header").find_next_sibling()
    lst = [data.text for data in datas]
    return '\n'.join(lst)  # Распаковываем список


def main():
    """Содержит url адреса и функций которые считывают и выводят данные с, интернет ресурса"""
    url_1 = 'https://python-teach.ru/uroki-po-python/metody-strok-v-python/?ysclid=lp8ixaoxyg510718927'
    url_2 = 'https://python-teach.ru/uroki-po-python/metody-slovarej-v-python/'
    print(get_data_1(practice_html_1(url_1)))
    print(get_data_2(practice_html_2(url_2)))


if __name__ == '__main__':
    main()
