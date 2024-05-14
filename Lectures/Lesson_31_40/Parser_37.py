import requests
from bs4 import BeautifulSoup


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        news = self.html.find_all('div', class_='caption')
        for new in news:
            title = new.find('h3').text
            href = new.find('h3').find('a').get('href')
            author = new.find('a', class_='topic-info-author-link').text.strip()
            self.res.append({'title': title,
                             'href': href,
                             'author': author,
                             })
        print(self.res)

    def save(self):
        with open(self.path, 'w', encoding='UTF-8') as f:
            i = 1
            for item in self.res:
                f.write(f"Новость № {i}\nНазвание: {item['title']}\nСсылка: {item['href']}\n"
                        f"Автор: {item['author']}\n\n{'*' * 30}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

