import time
import threading
import concurrent.futures
from pytube import YouTube

threading_local = threading.local()

def service(destino):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_video, destino)

def download_video(destino):
    urls_video = ['https://www.youtube.com/watch?v=3GQvsthnjeE','https://www.youtube.com/watch?v=mcWXvFC45hc','https://www.youtube.com/watch?v=AnSM63vhtXI','https://www.youtube.com/watch?v=lYdXgHbnQX4','https://www.youtube.com/watch?v=VuDc8HQ3Rbg']
    for link in urls_video: 
     yt = YouTube(link)
     video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
     save_video(video,destino)


def save_video(video,destino):
    video.download(destino)
    print("Se ha descargado los videos"+destino)


if __name__ == "__main__":
    init_time = time.time()
    destino = ["C:/Users/USER/Desktop/9 Cuatrimestre/Programacion Concurrente/1 Corte/Example 1/Videos"]
    service(destino)
    end_time = time.time()-init_time
    print(end_time)
