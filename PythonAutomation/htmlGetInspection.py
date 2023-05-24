import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_=('author'))
tags = soup.find_all('div', class_=('tags'))
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[1].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print("Tag:" + quoteTag.text)

