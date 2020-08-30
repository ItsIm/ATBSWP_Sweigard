# Python 3.8
# Играем в 2048 автоматически

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'/home/user/Downloads/geckodriver')
browser.get('https://play2048.co/')

htmlElement = browser.find_element_by_tag_name('html')
while True:
    htmlElement.send_keys(Keys.UP)
    htmlElement.send_keys(Keys.RIGHT)
    htmlElement.send_keys(Keys.DOWN)
    htmlElement.send_keys(Keys.LEFT)
    try:
        if browser.find_element_by_class_name('game-over'):
            print('Game over!')
            time.sleep(4)
            browser.close()
    except:
        pass
