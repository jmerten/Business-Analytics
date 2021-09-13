# M5: HTML Scraping
# Created by Jason Merten

import requests
from bs4 import BeautifulSoup

html_path = 'http://publicinterestlegal.org/county-list/'
html_doc = requests.get(html_path,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41'}).content

parsed = BeautifulSoup(html_doc,'lxml')
target = parsed.find_all('tr')

print('W&M Username: Jmerten')
print('Number of sublists: ',len(target))
data = []
for i in target:
    new_r = []
    for x in i.find_all('td'):
        new_r.append(x.text)
    data.append(new_r)
print('All Data:')
[print(i) for i in data]


