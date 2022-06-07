import sys
from time import sleep
import os
from random import randint

os.system('')

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

progress = 0

command = str(input('terminal@windows:~$ '))

if command =='sudo connect database':
    sleep(1)
    sys.stdout.write("Downloading progress (%d%%)   \r" % (progress) + style.YELLOW)
    sys.stdout.flush()

else:
    print('ERROR' + style.RED)
    sleep(2)
    os.system(os.close)

sleep(1)
for i in range(100):
    sleep(0.1)
    print('Downloading progress (%d%%)\r'%i, end="" +style.YELLOW)
    
sleep(1)


