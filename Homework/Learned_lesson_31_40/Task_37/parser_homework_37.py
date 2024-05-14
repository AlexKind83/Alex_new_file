import requests
from bs4 import BeautifulSoup


class Parser:
    """Класс который парсит несколько https страниц и записывает их в файл"""
    html = ''
    dict_pars = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        """Считывает url(https) адрес, и передает данные для дальнейшего считывания"""
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        """Парсинг данных, и записывает в dict_pars создавая словарь."""
        news = self.html.find_all('div', class_='post-card__title')
        for new in news:
            heading = new.find('span').text
            address = new.find('span').find('a').get('href')
            description = new.find_next('div', class_='post-card__description').text
            self.dict_pars.append({'heading': heading,
                                   'address': address,
                                   'description': description,
                                   })
            print(self.dict_pars)

    def save_file_homework(self):
        """Сохраняет данные в файл"""
        with open(self.path, 'w', encoding='UTF-8') as fw:
            count = 0
            for item in self.dict_pars:
                count += 1
                fw.write(f'Раздел Python № {count}\n'
                         f'Заголовок: {item["heading"]}\n'
                         f'Краткое описание: {item["description"]}\n'
                         f'Ссылка: {item["address"]}\n\n')

    def run(self):
        """Вызываемые функций.
        Передаются в модуль parser_start_homework_37."""
        self.get_html()
        self.parsing()
        self.save_file_homework()
