from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import os
import wget


pag = str(input('Insira o link da página: '))
print(pag)

browser = webdriver.Chrome()

browser.get("http://instagram.com")

username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.send_keys("granfinoshitpost")
password.send_keys('90124478edumes')

submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

submit.click()
keyword = "mmemes"
sleep(5)
browser.get(pag)
sleep(2)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)



images = browser.find_elements_by_tag_name('img')

images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path, keyword[1:])

os.mkdir(path)

counter = 0 

for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter)+ '.jpg')
    wget.download(image, save_as)
    counter +=1







browser.quit(sleep(200))




