import PySimpleGUI as sg 
from pytube import YouTube
import os

def window():
    sg.theme("DarkBrown4")
    layout = [ 
        [sg.Text("Youtube MP3 Downloader")]
    ]