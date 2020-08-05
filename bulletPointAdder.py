#! python3
# Копирует текст из буфера, добавляет в начале каждой новой строки * и пробел, копирует в буфер.

import pyperclip


text = pyperclip.paste().split('\n')
newText = []
for i in text:
	newText.append('* ' + i)
pyperclip.copy('\n'.join(newText))
print('Успешно скопировано в буфер.')
