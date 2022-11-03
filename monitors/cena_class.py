import threading
import time

PERSONAS = 8
COMER_CONTA = 100

class Persona(threading.Thread):
    palillos = []
    conta = 0

    def _init_(self):
        super(Persona, self)._init_()
        self.id = Persona.conta
        Persona.conta += 1
        Persona.palillos.append(threading.Lock())

    def derecha(self):
        resultado = ((self.id + 1) % PERSONAS)
        # print(str(resultado))
        return (self.id + 1) % PERSONAS

    
    def palillo(self):
        if self.id > self.derecha():
            Persona.palillos[self.id].acquire()
            Persona.palillos[self.derecha()].acquire()
        else:
            Persona.palillos[self.derecha()].acquire()
            Persona.palillos[self.id].acquire()

    def release(self):
        Persona.palillos[self.id].release()
        Persona.palillos[self.derecha()].release()

    
    def espera(self):
        time.sleep(0.15)

    
    def comer(self):
        print("{} Comiendo: ".format(self.id))
        time.sleep(0.30)
        print("{} Terminando de comer".format(self.id))

    
    def run(self):
        for i in range(COMER_CONTA):
            self.espera()
            self.palillo()
            self.comer()
            self.release()

def main():
    personas = []

    for i in range(PERSONAS):
        personas.append(Persona())

    for p in personas:
        p.start()
    
    for p in personas:
        p.join()

if __name__ == "__main__":
    main()