#! python3
# passwordManager.py - программа для незащищенного хранения паролей

PASSWORDS = {'email': 'fDFhjdH-34',
			  'blog': 'jGg56-_df',
			  'vk': 'IOEJfh4%ds32bf'}

import pyperclip, sys


def add_accoount(dictPassword):
	account = input('Введи название учетной записи:\n')
	password = input('Введи пароль:\n')
	done = dictPassword.setdefault(account, password)
	if done == password:
		print('Учетная запись добавлена успешно.')
	else:
		print('Учетная запись уже существует.')


def output_password(dictPassword, account):
	password = dictPassword.get(account, 0)
	if not password:
		print('Учетная запись не найдена. Повторите ввод.')
	else:
		pyperclip.copy(password)
		print(f'Пароль от учетной записи {account} скопирован в буфер.')


if len(sys.argv) < 2:
	print('Использование: python passwordManager.py [имя учетной записи] - копирование пароля')
	sys.exit()
output_password(PASSWORDS, sys.argv[1])
