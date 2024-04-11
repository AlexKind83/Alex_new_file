import requests
from bs4 import BeautifulSoup


def practice_html_1(url_1):
    r = requests.get(url_1)
    return r.text


def practice_html_2(url_2):
    r = requests.get(url_2)
    return r.text


def get_data_1(html):
    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.find('div', id="recent-posts-2").find_all('li')[1].text
    return datas


def get_data_2(html):
    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.find('div', class_="table-of-contents__header").find_next_sibling()
    lst = [data.text for data in datas]
    return '\n'.join(lst)


def main():
    url_1 = 'https://python-teach.ru/uroki-po-python/metody-strok-v-python/?ysclid=lp8ixaoxyg510718927'
    url_2 = 'https://python-teach.ru/uroki-po-python/metody-slovarej-v-python/'
    print(get_data_1(practice_html_1(url_1)))
    print(get_data_2(practice_html_2(url_2)))


if __name__ == '__main__':
    main()
