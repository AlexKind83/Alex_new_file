import requests
from bs4 import BeautifulSoup


class Parser2:
    html = ''

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        print(req)
        self.html = BeautifulSoup(req, 'lxml')

    def run(self):
        self.get_html()
