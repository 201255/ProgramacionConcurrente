import argparse
import threading
import time
import random

estadoPersona = None
candados = []
CANTIDAD_PERSONAS = 0 
RAFAGA_COMER = 0
TOTAL_TIEMPO_COMER = 0   
ESTADO_ESPERANDO = "F"
ESTADO_COMIENDO = "C"

def agarrarPalillos(id_persona):
    palillo_izq = candados[id_persona]
    palillo_der = candados[(id_persona - 1) % CANTIDAD_PERSONAS]

    palillo_izq.acquire()

    if palillo_der.acquire(blocking=False):
        return True
    else:
        palillo_izq.release()
        return False


def liberarPalillos(id_persona):
    candados[id_persona].release()
    candados[(id_persona - 1) % CANTIDAD_PERSONAS].release()


def iniciarCena(id_persona):
    intentos_fallidos = 0
    tiempo_comiendo = 0

    while tiempo_comiendo < TOTAL_TIEMPO_COMER:
        if agarrarPalillos(id_persona):
            intentos_fallidos = 0

            tiempo_comer = min(RAFAGA_COMER, TOTAL_TIEMPO_COMER - tiempo_comiendo)
            tiempo_comiendo += tiempo_comer
            print(f"[+] Persona {id_persona} comiendo [{tiempo_comer} seg.]")
            time.sleep(tiempo_comiendo)
            liberarPalillos(id_persona)

            estadoPersona[id_persona] = ESTADO_ESPERANDO
            tiempo_esperar = random.uniform(0, 5)
            print(f"[*] Persona {id_persona} Esperando[{tiempo_esperar:.2f} seg.]")
            time.sleep(tiempo_esperar)
        else:
            estadoPersona[id_persona] = ESTADO_ESPERANDO
            intentos_fallidos += 1
            
            tiempo_reintentar = random.uniform(0, 3)
            print(f"[ ] Persona {id_persona} esperando tenedores"
                f" Intento {intentos_fallidos} [{tiempo_reintentar:.2f} seg.]")
            time.sleep(tiempo_reintentar)
        
def obtenerArgumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num_personas", 
                        type=int, default=8, help="Número de personas (hilos)")
    parser.add_argument("-r", "--rafaga_comer", 
                        type=int, default=4, help="Ráfaga de comer de las personas")
    parser.add_argument("-t", "--tiempo_total", 
                        type=int, default=10, help="Tiempo total que requiere comer una persona para estar satisfecho")
    return parser.parse_args()


if __name__ == '__main__':
    args = obtenerArgumentos()
    
    CANTIDAD_PERSONAS = args.num_personas
    RAFAGA_COMER = args.rafaga_comer
    TOTAL_TIEMPO_COMER = args.tiempo_total
    
    estadoPersona = CANTIDAD_PERSONAS * [ESTADO_ESPERANDO]

    for _ in range(CANTIDAD_PERSONAS):
        candados.append(threading.RLock())

    hilos = []
    for i in range(args.num_personas):
        nuevo_hilo = threading.Thread(target=iniciarCena, args=(i,))
        hilos.append(nuevo_hilo)
    
    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()