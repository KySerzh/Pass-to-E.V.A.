from bs4 import BeautifulSoup
import requests
from requests import get
import time
import random

url = 'https://www.kinopoisk.ru/lists/movies/top250/?page='
houses = []
count = 1
while count <= 5:
    url = 'https://www.kinopoisk.ru/lists/movies/top250/?page=' + str(count)
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    house_data = html_soup.find_all('div', class_ = "styles_root__ti07r")
    if house_data != []:
        houses.extend(house_data)
    else:
        print('empty')
        break
    print('============')
    time.sleep(20)
    print('============')
    count += 1

print(len(houses))
print(houses[0])
print()
n = int(len(houses)) - 1
count = 0
while count <= 249:  # count <= n
    info = houses[int(count)]
    number = info.find('span', {"class": "styles_position__TDe4E"}).text
    title = info.find('span', {"class": "styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj"}).text
    mark = info.find('span', {"class": "styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg"}).text
    all_info = str(number) + " " + title + " " + str(mark)
    
    with open('all_info.txt', 'a') as file:
        file.write(all_info.text)
        
    
    count += 1

