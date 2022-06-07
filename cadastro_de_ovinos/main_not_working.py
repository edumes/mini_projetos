import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkGreen5')

EXCEL_FILE = 'cadastrados.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
        [sg.Text('Número:'),sg.Input(size=(3,0), key='numero')],
        [sg.Radio('Macho', 'cartoes', key='ehMacho'),sg.Radio('Femea', 'cartoes', key='ehFemea')],
        [sg.Text('Pai'),sg.Input(size=(10,0), key='pai')],
        [sg.Text('Mae'),sg.Input(size=(3,0), key='mae')],
        [sg.Button('Cadastrar')]
    ]

window = sg.Window('Cadastro de Ovinos', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Cadastrar':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Cadastro feito com sucesso!')
        clear_input()
window.close()