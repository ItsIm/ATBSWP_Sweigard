# Python 3.8
# Открывает бразер, логинится на сайте электронной почты и отправляет email с указанным текстом по указанному адресу

import sys
from selenium import webdriver

# Проверка наличия аргументов командной строки
if len(sys.argv) < 3:
    print('Пример ввода: python sendMail.py <login> <password> <recipient> <subject> <text>')
    sys.exit()

# Авторизация в аккаунте электронной почты
browser = webdriver.Firefox(executable_path=r'/home/user/Downloads/geckodriver')
browser.get('https://www.xmail.net/')
assert 'XMAIL' in browser.title

email = browser.find_element_by_id('username')
email.send_keys(sys.argv[1])
password = browser.find_element_by_id('password')
password.send_keys(sys.argv[2])
password.submit()

# Отправка сообщения


