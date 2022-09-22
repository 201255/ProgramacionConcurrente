import threading
from pytube import YouTube


mutex = threading.Lock()
def descarga(vid):
    yt = YouTube(vid)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    print("video descargado en: "+destino)

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        video=id
        self.id=video


    def run(self):
        mutex.acquire()
        descarga(self.id)
        mutex.release()

destino=r"C:/Users/ADMIN/Desktop/ProgramacionConcurrente/videos"
Hilos = [Hilo('https://www.youtube.com/watch?v=jhvfYsYQXkc'), Hilo('https://www.youtube.com/watch?v=i13yFolV-wk'), Hilo('https://www.youtube.com/watch?v=CH50zuS8DD0'), Hilo('https://www.youtube.com/watch?v=_ynU-Cm7uVU'),
Hilo('https://www.youtube.com/watch?v=3GQvsthnjeE'), Hilo('https://www.youtube.com/watch?v=AnSM63vhtXI'), Hilo('https://www.youtube.com/watch?v=kSv6qlPtvR0'), Hilo('https://www.youtube.com/watch?v=PQOyizaJ4u8'), Hilo('https://www.youtube.com/watch?v=x4KsG9wKLqo'),
Hilo('https://www.youtube.com/watch?v=mcWXvFC45hc')]
for h in Hilos:
    h.start()