import time
import pyautogui
import cv2
from datetime import datetime
import os

def entar(aula):
    time.sleep(1)
    os.startfile(aula)
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'd')
    time.sleep(0.5)
    pyautogui.click(x=1356, y=589)

semana = datetime.now().weekday()
horas = datetime.now().hour
min = datetime.now().minute

# Segunda:
if semana == 0:
    if horas >= 9 and horas <=11:
        aula="link da aula"
        entar(aula)
    elif horas > 11 and horas <=13:
        aula="link da aula"
        entar(aula)
# Terça:
elif semana == 1:
    if horas >= 7 and horas <=9:
        aula="link da aula"
        entar(aula)
    elif horas >= 11 and horas <=13:
        aula="link da aula"
        entar(aula)
# Quarta:
elif semana == 2:
    if horas >= 9 and horas <=11:
        aula="link da aula"
        entar(aula)
    elif horas > 11 and horas <=13:
        aula="link da aula"
        entar(aula)
# Quinta:
elif semana == 3:
    if horas >= 7 and horas <=9:
        aula="link da aula"
        entar(aula)
    elif horas >= 11 and horas <=13:
        aula="link da aula"
        entar(aula)
# Sexta:
elif semana == 4:
    if horas >= 7 and horas <=13:
        aula="link da aula"
        entar(aula)
# Sabado/Domingo:
elif semana == 5 or semana == 6:
    print(f'Rlxxx, a gnt tá no Fim de Semana... Não tem aula...')



