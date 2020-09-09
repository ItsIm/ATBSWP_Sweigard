from selenium import webdriver


browser = webdriver.Firefox(executable_path=r'/home/user/Downloads/geckodriver')
browser.get('https://mail.ru')

try:
    elem = browser.find_element_by_id("q")
    elem.send_keys('TOP')
    elem.submit()
except:
    print('Не удалось найти элемент.')