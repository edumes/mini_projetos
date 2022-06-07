import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
from pytube import YouTube
import os
#---------------------------------------------------------------------------------------------------
def window_url():  #janela para inserir o link
    sg.theme('DarkBrown4')
    layout = [
        [sg.Text('YouTube Downloader', font=('Courier, 16'))],
        [sg.Text('Link:'), sg.InputText(key='-URL-', text_color='orange')],
        [sg.Button('Download')]
    ]
    return sg.Window('Youtube Downloader', layout=layout, finalize=True, element_justification='c')

def window_res(): #janela para escolher a resolução
    sg.theme('DarkBrown4')
    layout = [
        [sg.Text('Escolha uma Resolução', font=('Courier, 16'))],
        [sg.Checkbox('360p', key='360p'), sg.Checkbox('720p', key='720p')],
        [sg.Button('Voltar'), sg.Button('Baixar Vídeo')]
    ]
    return sg.Window('Resolution', layout=layout, finalize=True, element_justification='c')

janela1, janela2 = window_url(), None
#---------------------------------------------------------------------------------------------------
def download_video_yt_360p(values):
    user = os.getenv("USERNAME")  #baixar video em 360p
    video = YouTube(url)
    video.streams.get_by_itag(18).download(rf"C:\Users\{user}\Downloads\Youtube")

def download_video_yt_720p(values):
    user = os.getenv("USERNAME")   #baixar video em 720p
    video = YouTube(url)
    video.streams.get_by_itag(22).download(rf"C:\Users\{user}\Downloads\Youtube")
#---------------------------------------------------------------------------------------------------
while True: #loop de leitura de eventos
    window, event, values = sg.read_all_windows()

    
    url = values.get['-URL-']
    sg.popup(url)
    
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == 'Download':
        janela2 = window_res()
    
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == 'Baixar Vídeo':
        if values['360p'] == True and values['720p'] == True:
            sg.popup('Escolha apenas uma das resoluções')
        elif values['360p'] == False and values['720p'] == False:
            sg.popup('Escolha uma das resoluções')
        elif values['360p'] == True:
            download_video_yt_360p(url)
            sg.popup('Download concluído com sucesso!')
            break
        elif values['720p'] == True:
            download_video_yt_720p(url)
            sg.popup('Download concluído com sucesso!')
            break
#---------------------------------------------------------------------------------------------------
window.close()
