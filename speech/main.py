import speech_recognition as sr
import pyautogui
from time import sleep
import os


#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Diga o que deseja: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")
            ouvir_microfone()
            if "1 abas" in frase:
                pyautogui.hotkey('ctrl', 't')
            
            

        if "pesquisar" in frase:
            os.system("start Chrome.exe")
            sleep(3)
            pyautogui.click(x=934, y=412)
            
            
        if "discord" in frase:
            pyautogui.hotkey("win")
            pyautogui.write("Discord")
            pyautogui.hotkey("enter")

        if "spotify" in frase:
            pyautogui.hotkey("win")
            pyautogui.write("Spotify")
            pyautogui.hotkey("enter")

        

        
        #Retorna a frase pronunciada
        print("Você disse: " + frase)
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase

ouvir_microfone()


    
        