# Python 3.8
# Заходит на сайт с картинками, осуществяет поиск по ключу и скачивает все результаты

import sys
import requests
import urllib3
import bs4
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Проверка наличия аргументов командной строки
if len(sys.argv) < 2:
    print('Пример ввода: python loadImg.py <tag> ')
    sys.exit()


# Переход на сайт Imgur
browser = webdriver.Firefox()
wait = WebDriverWait(browser, 500)
browser.get('https://imgur.com/')


# Поиск картинок по ключевому слову
searchTag = browser.find_element_by_class_name('Searchbar-textInput')
searchTag.send_keys(sys.argv[1])
searchTag.submit()

wait.until(EC.element_to_be_clickable((By.ID, "7Lsjz")))
url = browser.current_url


# Загрузка всех найденных картинок
urllib3.disable_warnings()
print(f'Загрузка страницы {url}')
res = requests.get(url, verify=False)

soup = bs4.BeautifulSoup(res.text, "html.parser")
linkImg = soup.select('.post a img')

for images in linkImg:
    fullLinkImg = f'https:{images.get("src")}'

    print(f'Загрузка картнки \033[35m{os.path.basename(fullLinkImg)}\033[0m')
    img = requests.get(fullLinkImg, verify=False)

    os.makedirs('imgur', exist_ok=True)
    file = open(os.path.join(r'source\imgur', os.path.basename(fullLinkImg)), 'wb')
    for chunc in img.iter_content(100000):
        file.write(chunc)
    file.close()
