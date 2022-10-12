from queue import Queue
from threading import Thread
import time

q = Queue(10)

def producer(name):
    
    count = 1 
    while True:
        q.join() 
        q.put(count)
        print(f"{name} está produciendo la proteina {count}")
        if count <= 9:
            count+=1
        else :
            break
def customer(name):
    
    count = 1
    while True:
        get = q.get()
        print(f"El consumidor {name} está consumiendo la proteina {count}")
        if count <= 9:
            count+=1
        else :
            break
        q.task_done() 
        time.sleep(1)

if __name__ == '__main__':
    t1 = Thread(target=producer,args=("Luis",))
    t2 = Thread(target=customer,args=("Yurandir",))
    t1.start()
    t2.start()