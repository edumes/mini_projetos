from PySimpleGUI import PySimpleGUI as sg

#interface grafica


sg.theme('Black')
layout = [
    [sg.Text('Insira o Link:'), sg.Input(key='link')],
    [sg.Button('Baixar')]
]

janela = sg.Window('Baixador de Videos', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break





    