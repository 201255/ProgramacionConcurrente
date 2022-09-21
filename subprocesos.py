import requests
import concurrent.futures
import threading
import mysql.connector
from pytube import YouTube

def get_services():
    x = 0
    for x in range(0, 50):
        response = requests.get('https://randomuser.me/api/')
        if response.status_code == 200:
            results = response.json().get('results')
            name = results[0].get('name').get('first')
            print(name)


def get_servicesPoke():

    url = 'https://pokeapi.co/api/v2/pokemon?limit=2000&offset=0'
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        results = data.get('results', [])
        if results:
            for x in results:
                pokename = x['name']
                write_db(pokename)

def write_db(pokename):
    conexion = mysql.connector.connect(
        user='root',
        password='feisima54321',
        host='localhost',
        database='Pokemones',
        port='3306'
    )
    mycursor = conexion.cursor()
    sql = "INSERT INTO poke(pokename) VALUES ('{0}')".format(pokename)
    mycursor.execute(sql)
    conexion.commit()

def download_video():
    urls_video = ["https://www.youtube.com/watch?v=3GQvsthnjeE","https://www.youtube.com/watch?v=mcWXvFC45hc","https://www.youtube.com/watch?v=AnSM63vhtXI","https://www.youtube.com/watch?v=lYdXgHbnQX4","https://www.youtube.com/watch?v=VuDc8HQ3Rbg"]
    destino = ("C:/Users/USER/Desktop/9 Cuatrimestre/Programacion Concurrente/1 Corte/Example 1/Videos")
    for link in urls_video:
      yt = YouTube(link)
      video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
      save_video(video,destino)


def save_video(video,destino):    
    video.download(destino)
    print("Se ha descargado los videos"+destino)    

if __name__ == '__main__':
    th1 = threading.Thread(target=get_services)
    th2 = threading.Thread(target=download_video)
    th3 = threading.Thread(target=get_servicesPoke)

    th2.start()
    th3.start()
    th1.start()

    th1.join()
    th2.join()
    th3.join()
    print("finalizado")



