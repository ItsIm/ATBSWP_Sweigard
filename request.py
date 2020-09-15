# Программа скачивает комиксы с сайта xkcd и сохраняет их на жестком диске

import bs4
import os
import requests

url = 'https://www.xkcd.com/10/'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
	#     Загрузка страницы
	print(f'Загрузка страницы {url}...')
	res = requests.get(url, verify='/home/user/Downloads/gca.crt')

	#     Поиск картинки
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	linkImg = soup.select('#comic img')[0]
	fullLinkImg = f"https:{linkImg.get('src')}"

	#     Выгрука картинки
	img = requests.get(fullLinkImg, verify='/home/user/Downloads/gca.crt')
	file = open(os.path.join(r'source/xkcd', os.path.basename(fullLinkImg)), 'wb')
	for chunk in img.iter_content(100000):
		file.write(chunk)
	file.close()

	#     Получение адреса кнопки Prev
	getLinkPrev = soup.select('a[rel="prev"]')[0]
	url = f"https://www.xkcd.com{getLinkPrev.get('href')}"
