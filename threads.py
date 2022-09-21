import requests
import threading
import time

def get_services(x=0):
    time.sleep(0.5)
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)

if __name__ == '__main__':
    x=0
    for x in range(0,20):
        th1 = threading.Thread(target=get_services, args=[x])
        th1.start()
        #get_services()


# descarar 5 videos , escribir 2000 registros, generar una solicitud a random user de 50 usuarios