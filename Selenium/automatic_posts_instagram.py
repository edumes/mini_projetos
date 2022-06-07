from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()

chrome.get('https://www.instagram.com/')
sleep(5)