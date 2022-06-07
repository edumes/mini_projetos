from typing import Text
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('diga algo: ')
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='pt-BR')
        print('vc disse: '+ text)
    except:
        print('nao entendi')

