import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
from pytube import YouTube
import moviepy.editor as mp
import os

sg.theme('DarkBrown4')
layout = [
    [sg.Text('YouTube MP3 Converter', font=('Courier, 18'))],
    [sg.Text('Link:', font=('Courier, 14')), sg.InputText(key='-URL-', text_color='orange')],
    [sg.Button('Converter Video')]
]
window = sg.Window('Youtube MP3 Converter', layout=layout, element_justification='c')

def mp3():
    user = os.getenv("USERNAME")
    video = YouTube(url).streams.get_audio_only()
    video.download(rf"C:\Users\{user}\Downloads\Youtube MP3")
    title = str(video.title)
    clip = mp.AudioFileClip(rf"C:\Users\{user}\Downloads\Youtube_MP3\{title}.mp4")
    clip.write_audiofile(rf"C:\Users\{user}\Downloads\Youtube_MP3\{title}.mp3")
    os.remove(rf"C:\Users\{user}\Downloads\Youtube_MP3\{title}.mp4")

while True: #loop de leitura de eventos
    event, values = window.read()
    url = values.get('-URL-')

    if window and event == sg.WIN_CLOSED:
        break
    
    if event in window == 'Converter Video':
        mp3()
        sg.popup('Download concluído com sucesso, seu video foi baixado na pasta downloads')