# from threading
import threading
from time import sleep

mutex = threading.Lock()

def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id


    def run(self):
        mutex.acquire()
        # sleep(3-self.id)
        crito(self.id)
        # print("valor" + str(self.id))
        mutex.release()




hilos = [Hilo(1), Hilo(2),Hilo(3)]
x=1;
for t in hilos:
    t.start()