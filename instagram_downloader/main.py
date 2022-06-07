import PySimpleGUI as sg
import instaloader as ig
import requests
import re

def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text

url = input('>>')
response = get_response(url)