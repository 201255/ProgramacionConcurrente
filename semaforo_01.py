from threading import Thread, Semaphore
from turtle import st
from pytube import YouTube
import requests

# Descarga Video
def download_video():
    urls_video = ["https://www.youtube.com/watch?v=3GQvsthnjeE"]
    destino = ("C:/Users/USER/Desktop/9 Cuatrimestre/Programacion Concurrente/1 Corte/Example 1/Videos")
    # for link in urls_video:
    yt = YouTube(urls_video)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
    save_video(video,destino)


def save_video(video,destino):    
    video.download(destino)
    print("Se ha descargado los videos"+destino)


# Descarga Musica
def download_music():
    urls_music = ["https://www.youtube.com/watch?v=3GQvsthnjeE"]
    destino2 = ("C:/Users/USER/Desktop/9 Cuatrimestre/Programacion Concurrente/1 Corte/Example 1/music")
    # for link in urls_video:
    yt = YouTube(urls_music)
    music = yt.streams.filter(only_audio=True).first()
    save_video(music,destino2)


def save_video(music,destino2):    
    music.download(destino2)
    print("Se ha descargado los videos"+destino2)


# Descarga Imagen
def download_image():
    url_imagen = "https://golang.org/doc/gopher/appenginegophercolor.jpg" # El link de la imagen
    destino = ("C:/Users/USER/Desktop/9 Cuatrimestre/Programacion Concurrente/1 Corte/Example 1/image")
    nombre_local_imagen = "go.jpg"
    imagen = requests.get(url_imagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
    save_imagen(imagen,destino)


def save_imagen(imagen,destino):    
    imagen.download(destino)
    print("Se ha descargado la imagen")
    
if __name__ == "__main__":
    download_video()  