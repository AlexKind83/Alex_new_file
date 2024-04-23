import requests
from bs4 import BeautifulSoup
import re


class Parser:
    html = ''

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        # print(req)
        self.html = BeautifulSoup(req, 'lxml')

    def parser(self):
        news = self.html.find('div', itemprop="name")
        print(news)



    def run(self):
        self.get_html()
        self.parser()
