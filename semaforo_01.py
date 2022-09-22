from threading import Thread, Semaphore
from pytube import YouTube
semaforo = Semaphore(1)


def descarga(vid):
    yt = YouTube(vid)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    print("video descargado en: "+destino)

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        video=id
        self.id=video

    def run(self):
        semaforo.acquire()
        descarga(self.id)
        semaforo.release()


destino=r"C:/Users/ADMIN/Desktop/ProgramacionConcurrente/videos"
threads_semaphore = [Hilo('https://www.youtube.com/watch?v=jhvfYsYQXkc'), Hilo('https://www.youtube.com/watch?v=i13yFolV-wk'), Hilo('https://www.youtube.com/watch?v=CH50zuS8DD0'), Hilo('https://www.youtube.com/watch?v=_ynU-Cm7uVU'),
Hilo('https://www.youtube.com/watch?v=3GQvsthnjeE'), Hilo('https://www.youtube.com/watch?v=AnSM63vhtXI'), Hilo('https://www.youtube.com/watch?v=kSv6qlPtvR0'), Hilo('https://www.youtube.com/watch?v=PQOyizaJ4u8'), Hilo('https://www.youtube.com/watch?v=x4KsG9wKLqo'),
Hilo('https://www.youtube.com/watch?v=mcWXvFC45hc')]
for t in threads_semaphore:
    t.start()

# from threading import Thread, Semaphore
# from turtle import st
# from pytube import YouTube
# import requests

# semaforo = Semaphore(1)

# def crito(id):
#     global x;
#     x = x + id
#     print("Hilo =" +str(id)+ " =>" + str(x))
#     x=1

# class Hilo(Thread):
#     def __init__(self, id):
#         Thread.__init__(self)
#         self.id=id

#     def run(self):
#         semaforo.acquire()
#         crito(self.id)
#         semaforo.release()

# # Descarga Video
#     def download_video():
#         urls_video = ['https://www.youtube.com/watch?v=3GQvsthnjeE']
#         destino = ("C:/Users/ADMIN/Desktop/ProgramacionConcurrente/videos")
#         for link in urls_video:
#             yt = YouTube(link)
#             video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
#             save_video(video,destino)


#         def save_video(video,destino):    
#             video.download(destino)
#             print("Se ha descargado los videos"+destino)


# # Descarga Musica
#     def download_music():
#         urls_music = ["https://www.youtube.com/watch?v=3GQvsthnjeE"]
#         destino2 = ("C:/Users/ADMIN/Desktop/ProgramacionConcurrente/music")
#         for link2 in urls_music:
#             yt = YouTube(link2)
#             music = yt.streams.filter(only_audio=True).first()
#             save_music(music,destino2)


#         def save_music(music,destino2):    
#             music.download(destino2)
#             print("Se ha descargado los videos" + destino2)


# # Descarga Imagen
#     def download_image():
#         url_imagen = "https://golang.org/doc/gopher/appenginegophercolor.jpg" # El link de la imagen
#         destino = ("C:/Users/ADMIN/Desktop/ProgramacionConcurrente/image")
#         nombre_local_imagen = "go.jpg"
#         imagen = requests.get(url_imagen).content
#         with open(nombre_local_imagen, 'wb') as handler:
#             handler.write(imagen)
#             save_imagen(imagen)
    
    
#         def save_imagen(imagen):    
#             print("Se ha descargado la imagen")
    
    
#     def get_service():
#         x=0
#         for x in range(0,1):
#             response = requests.get('https://randomuser.me/api/')
#         if response.status_code == 200:
#             results = response.json().get('results')
#             name = results[0].get('name').get('first')
#             print(name)



# threads_semaphore = [Hilo(1), Hilo(2), Hilo(3), Hilo(4)]
# x=1;
# for t in threads_semaphore:
#     t.start()


    
# # if __name__ == "__main__":
# #     get_service()  