import random, os


states = {'Айдахо': 'Центр Бойсе', 'Айова': 'Основной центр Де-Мойн', 'Алабама': 'Монтгомери',	'Аляска': 'Центр Джуно',\
	   'Аризона': 'Столичный район Финикс','Арканзас': 'Литл-рок', 'Вайоминг': 'Шайен','Вашингтон': 'Олимпия',\
	   'Вермонт': 'Монтпилиер',	'Виргиния': 'Ричмонд','Виргиния Западная': 'Чарлстон'}


def generating_ticket(states):
	listStates = list(states.keys())
	random.shuffle(listStates)
	listCapitals = list(states.values())
	ticket = ''
	for i in listStates:
		random.shuffle(listCapitals)
		answerChoice = [states[i]]
		for j in range(3):
			answerChoice.append(listCapitals[j])
			while answerChoice.count(listCapitals[j]) > 1:
				answerChoice.pop()
				answerChoice.append(random.choice(listCapitals))
		random.shuffle(answerChoice)
		answerChoice = ', '.join(answerChoice)
		ticket += f'{i}: {answerChoice}\n'
	return ticket


def save_ticket_in_file(filename, text):
	file = open(filename, 'w')
	file.write(text)
	file.close()
	return True


if os.path.exists('.\\tickets'):
	os.chdir('.\\tickets')
else:
	print('Папка создана.')
	os.makedirs('.\\tickets')
	os.chdir('.\\tickets')

for i in range(len(states.keys())):
	filenames = f'ticket №{i}.txt'
	ticket = generating_ticket(states)
	if ticket:
		print(f'Билет №{i} успешно сгенерирован.')

	if save_ticket_in_file(filenames, ticket):
		print(f'Файл {filenames} успешно создан.')
		