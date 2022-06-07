from pytube import *
from PIL import Image
import requests, os, time

class BaixaVideo:
    def __init__(self, url):
        self._url, self._video = self.valida_url(url)
        self._titulo = self._video.title
        self._duracao = self._video.length
        self._rating = self._video.rating
        self.tracking = self._video.vid_info['trackingParams']
        self._views = self._video.views 
        self._thumbnail_url = self._video.thumbnail_url


    def get_informacoes(self, info):
        informacoes = {"titulo": self._titulo,
                       "duracao": self._duracao,
                       "views": self._views,
                       "likes": self._rating }
        if info in informacoes:
            return informacoes[info]
        else:
            return "Erro de digitacao"

    def valida_url(self, url):
        if url != '':
            url_true = url
            try:
                video_true = YouTube(url_true)
            except Exception:
                raise ValueError("Algum erro aconteceu hehe!")
            return (url_true, video_true)
        else:
            raise ValueError("O campo de url deve ser preenchido!")
        
    def __str__(self):
        frase = (f"Titulo: {self._titulo}\n"
                f"Duracao: {self._duracao} - Views: {self._views} - Likes: {self._rating}")
        return frase

    @property
    def get_videos(self):
        self.lista_videos = self._video.streams.filter(file_extension="mp4").order_by("resolution")
        return self.lista_videos
    
    def baixe_mp3(self, path):
        video = self._video.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=path, filename_prefix="Audio ")
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
    
    @property
    def get_minima_resolucao(self):
        videos = self.get_videos
        return videos.get_lowest_resolution()

    @property
    def get_maxima_resolucao(self):
        videos = self.get_videos
        return videos.get_highest_resolution()

    def get_thumbnail(self):
        caminho_padrao = os.path.join(os.path.dirname(__file__), f'img\\{self.tracking}_thumbnail.png')
        img = requests.get(self._thumbnail_url, stream=True).content
        try:
            with open(caminho_padrao, "wb") as handler:
                handler.write(img)
            del img
            return caminho_padrao
        except: 
            return "erro"
    
    def padroniza_thumb(self, tamanho=(480,360)):
        caminho_padrao = os.path.join(os.path.dirname(__file__), f'img\\{self.tracking}_thumbnail_resized.png')
        thumb = self.get_thumbnail()
        with Image.open(thumb) as im:
            irm = im.resize(tamanho)
            irm.save(caminho_padrao, "PNG")
            os.remove(thumb)
        return caminho_padrao

    def download(self, ext, local, tipo="720p"):
        if ext == "mp4":
            if tipo == "720p":
                self.get_maxima_resolucao.download(local)
            if tipo == "360p":
                self.get_minima_resolucao.download(local)
            time.sleep(1)
        if ext == "mp3":
            self.baixe_mp3(local)
            time.sleep(1)


class DeletaThumb:
    def __init__(self, thumbs):
        if isinstance(thumbs, list):
            for thumb in thumbs:
                os.remove(thumb)
        else:
            os.remove(thumbs)

if __name__ == "__main__": 
    video = BaixaVideo("https://www.youtube.com/watch?v=8bObaGeeiFk")
    video.padroniza_thumb()

 #print(f'img\\{video.get_informacoes("titulo").strip("")}_thumbnail.png')