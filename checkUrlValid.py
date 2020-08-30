# Python 3.8
# Проверяет на валидность все ссылки на указанной странице

import webbrowser
import urllib3
import requests
import bs4

url = 'https://www.google.com/search?hl=en&q=element_to_be_clickable%20selenium'
urllib3.disable_warnings()

res = requests.get(url, verify=False)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')
print(links)
for link in links:
    try:
        url = f'https://www.google.com{link.get("href")}'
        res = requests.get(url, verify=False)
        if res.status_code == 200:
            print(f'\033[32m200 {url}\033[0m')
        else:
            print(f'\033[31m404 {url}\033[0m')
    except:
        pass
