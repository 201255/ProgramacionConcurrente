import time
from threading import Thread
import requests


def service_url(url):

   x = requests.head(url)
   if  x.status_code != 200:
      print(str(url) + 'Sitio Web Inactivo: ' +str(x.status_code)) 
   else:
      print(str(url) + 'Sitio Web Activo: ' +str(x.status_code))


class Hilo(Thread):
   def __init__(self, url):
      Thread.__init__(self)
      self.url = url

   def run(self):
      service_url(self.url)


t1 = [
   Hilo('https://www.facebook.com/'), Hilo('https://www.canva.com/es_419/'),
   Hilo('https://www.google.com'), Hilo('https://www.logitech.com/es-mx    '), Hilo('https://www.behringer.com/'),
   Hilo('https://www.instagram.com'), Hilo('https://www.amazon.com.mx/'), Hilo('https://trello.com/'), 
   Hilo('https://www.youtube.com/'), Hilo('https://www.netflix.com/mx/'), Hilo('https://www.disneyplus.com/es-mx'), 
   Hilo('https://open.spotify.com/'), Hilo('https://www.akg.com/'), Hilo('https://www.nike.com/mx/'), 
   Hilo('https://www.shure.com/es-ES'), Hilo('https://web.telegram.org/'), Hilo('https://discord.com/'), 
   Hilo('https://www.jetbrains.com/idea/'), Hilo('https://code.visualstudio.com/'), Hilo('https://web.whatsapp.com/'), 
   Hilo('https://www.raspberrypi.com/software/'), Hilo('https://twitter.com/'), Hilo('https://www.tiktok.com/es'),
   Hilo('https://www.tinkercad.com/'), Hilo('https://row.hyperx.com/')
]

while True:
   for i in t1:
      i.start()
   time.sleep(240) 