import requests
from bs4 import BeautifulSoup


def search():
    url = 'https://www.w3schools.com/'
    req = requests.get(url).text
    # html = BeautifulSoup(req, 'lxml')
    print(req)


search()
