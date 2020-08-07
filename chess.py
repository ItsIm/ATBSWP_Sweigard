# Играем в крестики-нолики

import sys


map = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
	   'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
	   'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def prints(obj):
	print(f'{map["top-L"]}|{map["top-M"]}|{map["top-R"]}')
	print('-+-+-')
	print(f'{map["mid-L"]}|{map["mid-M"]}|{map["mid-R"]}')
	print('-+-+-')
	print(f'{map["low-L"]}|{map["low-M"]}|{map["low-R"]}')


def check():
	checkMap = list(map.values())
	if checkMap[0] == checkMap[1] == checkMap[2] != ' ':
		print(f'Поздравляю! Победил игрок {checkMap[0]}')
		sys.exit()
	elif checkMap[3] == checkMap[4] == checkMap[5] != ' ':
		print(f'Поздравляю! Победил игрок {checkMap[3]}')
		sys.exit()
	elif checkMap[6] == checkMap[7] == checkMap[8] != ' ':
		print(f'Поздравляю! Победил игрок {checkMap[6]}')
		sys.exit()
	elif checkMap[0] == checkMap[4] == checkMap[8] != ' ':
		print(f'Поздравляю! Победил игрок {checkMap[0]}')
		sys.exit()
	elif checkMap[2] == checkMap[4] == checkMap[6] != ' ':
		print(f'Поздравляю! Победил игрок {checkMap[2]}')
		sys.exit()
	elif checkMap[0] == checkMap[3] == checkMap[6] != ' ':
		print(f'Поздравляю! Победил игрок {checkMap[0]}')
		sys.exit()
	elif checkMap[1] == checkMap[4] == checkMap[7] != ' ':
		print(f'Поздравляю! Победил игрок {checkMap[1]}')
		sys.exit()
	elif checkMap[2] == checkMap[5] == checkMap[8] != ' ':
		print(f'Поздравляю! Победил игрок {checkMap[2]}')
		sys.exit()


def help():
	print('Названия полей:')
	print(list(map.keys()))


def entry(gamer):
	check()
	print(f'Ход игрока {gamer}.')
	while True:
		field = input('Выбери поле для ввода:\n')
		if field in map:
			break
		elif field == 'exit':
			sys.exit()
		elif field == 'help':
			help()
		else:
			print('Нет такого!')

	if map[field] != ' ':
		print('Поле занято!')
	else:
		map[field] = gamer
		prints(map.values())


gamer = 'X'
for i in range(9):
	entry(gamer)
	if gamer == 'X':
		gamer = '0'
	else:
		gamer = 'X'

print('Ничья!')
