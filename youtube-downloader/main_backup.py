import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
from pytube import YouTube
import os
#---------------------------------------------------------------------------------------------------
def window_link():  #janela para inserir o link
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
        [sg.Button('360p', key='360p'), sg.Button('720p', key='720p')]
    ]
    return sg.Window('Resolution', layout=layout, finalize=True, element_justification='c')

janela1, janela2 = window_link(), None
#---------------------------------------------------------------------------------------------------
def download_video_yt_360p():  #baixar video em 360p
    video = YouTube(url)
    video.streams.get_by_itag(18).download()
    os.mkdir('Dowloads\\Youtube')

def download_video_yt_720p():   #baixar video em 720p
    video = YouTube(url)
    video.streams.get_by_itag(22).download()
#---------------------------------------------------------------------------------------------------
while True: #loop de leitura de eventos
    window, event, values = sg.read_all_windows()

    url = values.get('-URL-')
    print(url)
    
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    
    if event == 'Download':
        janela2 = window_res()  #ate aqui funfa
        
        if window == janela2 and event == '360p':
            download_video_yt_360p()
        else:
            download_video_yt_360p()
            

        if window == janela2 and event == '720p':
            download_video_yt_720p()
        else:
            download_video_yt_720p()
            
        sg.popup('Download concluído com sucesso!')
        
#---------------------------------------------------------------------------------------------------
window.close()
