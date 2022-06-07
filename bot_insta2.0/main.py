from selenium import webdriver
import pyautogui as pg

navegador = webdriver.Chrome()
navegador.get('https://www.instagram.com/accounts/emailsignup/')
navegador.switch_to.new_window('tab')
navegador.get('http://tempsky.com')
navegador.execute_script("window.scrollTo(2, document.body.scrollHeight);")
navegador.find_element_by_xpath('//*[@id="content"]/div[2]/form/div[1]/input')


