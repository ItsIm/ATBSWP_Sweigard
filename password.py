# Проверка пароля на сложность

import re
import sys


def check_password(password):
	if len(password) < 8:
		print('Пароль должен содержать минимум 8 символов!')
		sys.exit()

	regular1 = re.compile(r'\d+')
	regular2 = re.compile(r'[a-z]+')
	regular3 = re.compile(r'[A-Z]+')

	match1 = regular1.findall(password)
	match2 = regular2.findall(password)
	match3 = regular3.findall(password)

	if match1 and match2 and match3:
		print('Хороший пароль!')
	else:
		print('''Пароль должен содержать:
				 - символы в нижнем регистре
				 - символы в верхнем регистре
				 - как минимум 1 цифру''')

check_password('afddfd1Df')