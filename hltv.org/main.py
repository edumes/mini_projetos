from HLTV import *
import locale
from time import sleep
from rich import print
from utils.logo import logo
from rich.text import Text
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track

console = Console()

def process_data():
    sleep(0.00)

for _ in track(range(100), description='[green]Carregando HLTV.org'):
    process_data()

logo("HLTV . org")
print(Panel.fit("Desenvolvido por: Eduardo Santarosa"))
print("==============================================================================")
get_top_teams()
team = str(input("Digite o nome do time para saber seus resultados: ").upper())

if team == "IMPERIAL":
    print("imperial")
else:
    print("time não encontrado")

sleep(120)