import time
import threading
import concurrent.futures
from pytube import YouTube

threading_local = threading.local()

def service(urls_video):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_video, urls_video)

def download_video(urls_video):
    for link in urls_video:
     print(link)         
     yt = YouTube(link)
     video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
     save_video(video)


def save_video(video):
    destino = ["C:/Users/USER/Desktop/9 Cuatrimestre/Programacion Concurrente/1 Corte/Example 1/Videos"]
    video.download(destino)
    print("Se ha descargado los videos"+destino)


if __name__ == "__main__":
    init_time = time.time()
    urls_video = 'https://www.youtube.com/watch?v=3GQvsthnjeE','https://www.youtube.com/watch?v=tIpzfs5tBJU','https://www.youtube.com/watch?v=qcR1KbbhRTs','https://www.youtube.com/watch?v=lYdXgHbnQX4','https://www.youtube.com/watch?v=VuDc8HQ3Rbg'
    service(urls_video)
    end_time = time.time()-init_time
    print(end_time)
