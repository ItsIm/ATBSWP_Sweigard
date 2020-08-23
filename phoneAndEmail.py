# Программа принимает на вход текст из буфера обмена
# Ищет в тексте нужные конструкции
# Отправляет полученный текст в буфер обмена

import re
import pyperclip
import sys


text = pyperclip.paste()
if not text:
	print('Буфер обмена пуст!')
	sys.exit()

email = re.compile(r'[\w\d._-]+@[\w|\d]+.\w+')
# email = re.compile(r'[a-zA-Z0-9.%+-]+@[\w|\d]+.\w+')
phone = re.compile((r'\+\d{11}'))

match = email.findall(text)
print(match)
match += (phone.findall(text))
if not match:
	print('Совпадений не найдено!')
	sys.exit()

pyperclip.copy(','.join(match))

