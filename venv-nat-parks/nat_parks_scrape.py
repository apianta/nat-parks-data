import requests
from bs4 import BeautifulSoup
from csv import writer
import re

url = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'lxml')

tables = soup.find_all('table')[1]
rows = tables.find_all('tr')
# print(rows)


def get_parks():
    park_list = []
    for table in tables:
        ths = tables.find_all('th', scope='row')
        table_rows = tables.find_all('tr')
        for th in ths:
            parks = th.find('a').string
            print(parks)


def get_visitors():

    for table in tables:
        ths = tables.find_all('th', scope='row')
        cells = [i for i in tables.find_all('td', text=True)]
        for i in cells:
            visitors = []
            print(i.contents[0])


get_visitors()
V = []

for row in tables.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 5:
        V.append(cells[0].find(text=True))
        print(V)
