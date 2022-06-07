import os
import PySimpleGUI as sg
from baixarVideos import BaixaVideo, DeletaThumb

#cria o design da janela, botoes vermelhos, backgroud branco, etc...
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#ffffff',
                                        'TEXT': '#000000',
                                        'INPUT': '#e6e3e3',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#ff0000',
                                        'BUTTON': ('#ffffff', '#ff0000'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0, } 
sg.theme("MyCreatedTheme")

def cria_layout_download(tipo, titulo, thumb):
    layout_botao = sg.FolderBrowse("DOWNLOAD", size=(20,2),enable_events=True, key="-DOWNLOAD-")

    info = [ #layout do titulo e da thumbnail
    [sg.Text(titulo, size=(47,2), justification="center", pad=0)],
    [sg.Image(thumb, pad=0)]
    ]

    layout_mp4 = [ #layout da janela do mp4
        [sg.Text("Escolha a qualidade:"), sg.Radio("HD", "QUALITYS", key="-720p-", default=True), sg.Radio("SD", "QUALITYS", key="-360p-")],
        [layout_botao],
    ]

    layout_mp3 = [ #layout da janela do mp3
        [sg.Text("Baixe o audio: ")], 
        [layout_botao],  
    ]

    if tipo == "MP4": #escolhe entre os tipos de janela e combina os layouts, retornando o resultado
        layout_MP4 = [
        [sg.Column(info, justification="center", vertical_alignment="center", element_justification="center")], 
        [sg.HSep()], 
        [sg.Column(layout_mp4, justification="center", vertical_alignment="center", element_justification="center")]
        ]
        return layout_MP4
    if tipo == "MP3":
        layout_MP3 = [
        [sg.Column(info, justification="center", vertical_alignment="center", element_justification="center")], 
        [sg.HSep()], 
        [sg.Column(layout_mp3, justification="center", vertical_alignment="center", element_justification="center")]
        ]
        return layout_MP3


def layout():  
    #layout da janela primária e já retorna o objeto
    botao_youtube = os.path.join(os.path.dirname(__file__), r"img\youtube_logo.png")
    icone = [[sg.Image(botao_youtube, pad=0)]]
    titulo = [[sg.Text("YT DOWNLOADER", text_color="red", font=("impact", 45), justification="left", pad=0)]]

    layout_botoes = [
        [sg.Combo(["MP4", "MP3"], default_value="MP4", size=(10,2), readonly=True, key="-TIPO-"),
        sg.Button("ENVIAR", key="-ENVIAR-", size=(15, 1))]]

    layout = [
        [sg.Column(icone), sg.Column(titulo, justification="center")],
        [sg.Text("Coloque a url aqui: "), sg.Input(key="-URL-", size=(55, 1), pad=0)],
        [sg.Column(layout_botoes, justification="right", element_justification="right")], 
    ]
    return sg.Window("Downloader", layout)


def mp4_selector(caminho, values1, video):
    #dependendo da escolha baixa o video
    if values1["-360p-"]:
        video.download("mp4", caminho, "360p")
    if values1["-720p-"]:
        video.download("mp4", caminho, "720p")


def mp3(caminho,  video):
    video.download("mp3", caminho)


window = layout()

while True:
    events, values = window.read()
    if events in (sg.WIN_CLOSED, "Exit"):
        break
    try:
        video = BaixaVideo(values["-URL-"]) 
    except ValueError:
            sg.popup("URL inválida!")
    else:
        if events == "-ENVIAR-":
            thumbnail = video.padroniza_thumb((360, 300))
            tipo = values["-TIPO-"]
            layout_download = cria_layout_download(tipo, video.get_informacoes("titulo"), thumbnail )
            window_download = sg.Window("Download", layout_download)   
            events1, values1 = window_download.read()    #essas parte carrega a janela de download
            caminho = values1["-DOWNLOAD-"]

            if events1 in (sg.WIN_CLOSED, "Exit"):
                deleta = DeletaThumb(thumbnail)

            if events1 == "-DOWNLOAD-":
                if tipo == "MP3":
                    mp3(caminho, video)  #essa parte carrega o download
                if tipo == "MP4":
                    mp4_selector(caminho, values1, video)

window.close(); del window



