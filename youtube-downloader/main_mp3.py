from pytube import YouTube
import moviepy.editor as mp
import os
user = os.getenv("USERNAME")
url = input('URL: ')
ext = input('''[1] MP3
[2] MP4
-> ''')
if ext == '1':
    video = YouTube(url).streams.get_audio_only()
    video.download(rf"C:\Users\{user}\Desktop\mp3")
    title = str(video.title)
    clip = mp.AudioFileClip(rf"C:\Users\{user}\Desktop\mp3\{title}.mp4")
    clip.write_audiofile(rf"C:\Users\{user}\Desktop\mp3\{title}.mp3")
    os.remove(rf"C:\Users\{user}\Desktop\mp3\{title}.mp4")
elif ext == '2':
    print('Fazendo o download...')
    video = YouTube(url)
    video = video.streams.get_highest_resolution()
    video.download(rf"C:\Users\{user}\Desktop\mp4")
    print('Download Concluído')