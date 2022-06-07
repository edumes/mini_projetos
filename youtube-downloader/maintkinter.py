from tkinter import *
from pytube import YouTube
import moviepy.editor as mp
import os
user = os.getenv("USERNAME")

def mp4():
    url = entry.get()
    video = YouTube(url)
    video = video.streams.get_highest_resolution()
    video.download(rf"C:\Users\{user}\Desktop\mp4")
def mp3():
    url = entry.get()
    video = YouTube(url).streams.get_audio_only()
    video.download(rf"C:\Users\{user}\Desktop\mp3")
    title = str(video.title)
    clip = mp.AudioFileClip(rf"C:\Users\{user}\Desktop\mp3\{title}.mp4")
    clip.write_audiofile(rf"C:\Users\{user}\Desktop\mp3\{title}.mp3")
    os.remove(rf"C:\Users\{user}\Desktop\mp3\{title}.mp4")
root = Tk()
root.geometry('300x200')
root.title("F4 - Video/Audio Downloader")
#input
entry = Entry(root, width=50)
entry.pack(pady=15, padx=20)
entry.insert(0,'Cole aqui o link do video')
#botão
b1 = Button(root, text='MP3', command=mp3, bg='red', width= 15, height=2)
b1.pack(side=LEFT,padx=8)
b2 = Button(root, text='MP4', command=mp4, bg='red', width= 15, height=2)
b2.pack(side=RIGHT,padx=8)
root.mainloop()