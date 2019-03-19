import requests
import re
from bs4 import BeautifulSoup


def response_ok(res):
    content = res.headers['Content-Type'].lower()
    return (
            res.status_code == 200
            and content is not None
    )


def get_page(url):
    response = requests.get(url)
    if response_ok(response):
        return response.content
    else:
        return None

url = 'https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2'

raw_html = get_page(url)
html = BeautifulSoup(raw_html, 'html.parser')



coutries = {}
table = html.find('table',{'class':'wikitable sortable'}).find_all('td')
step = 0
for index,elm in enumerate(table):
    if 'id' in elm.attrs:
        code = elm.attrs['id']
    link = elm.find('a')
    if not link:
        continue
    if link.text[0] != '.' and link.text[:3] != 'ISO':
        country = link.text
        coutries.update({code: country})

print(coutries['FI'])