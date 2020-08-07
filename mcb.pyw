# Буфер обмена для работы с несколькими значениями

import pyperclip
import sys
import shelve


# Читать агрументы командной строки
#   Проверка наличия 3 аргументов(или 2)
#
# Чтение и запись из буфера обмена
#   Если 2 аргумент save, сохранять из значение из буфера с ключевым словом, которое идет 3 агрументом
#   Если list, скопировать в буфер все ключевые слова
#   Иначе скопировать текст, соответствующий ключу скопировать в буфер
#
# Сохранять и загружать текст в файл хранилища
# 	Записать новую пару ключ-значение в буфер, если есть

if len(sys.argv) < 2:
	print('Пример работы: python mcb.pyw [save|list|key] [newKey]')
	sys.exit()
elif sys.argv[1] in 'save' and len(sys.argv) < 3:
	print('Пример работы: python mcb.pyw [save|list|key] [newKey]')
	sys.exit()

argument = sys.argv[1]

if argument in 'save':
	print(f'Копируем текст из буфера и сохраняем в файл с ключом {sys.argv[2]}')
	textInFile = pyperclip.paste()
	shelvFile = shelve.open('mcb')
	shelvFile[sys.argv[2]] = textInFile
	shelvFile.close()

elif argument in 'list':
	print('Копируем в буфер все ключи')
	copyInBuffer = []
	with shelve.open('mcb') as shelveFile:
		for key in shelveFile.keys():
			copyInBuffer.append(key)
	pyperclip.copy('\n'.join(copyInBuffer))

else:
	print(f'Копируем в буфер значение для ключа {argument}')
	shelveFile = shelve.open('mcb')
	copyInBuffer = shelveFile[sys.argv[1]]
	pyperclip.copy(copyInBuffer)
	shelveFile.close()
