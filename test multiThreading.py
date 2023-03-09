import threading
import time

def numero_par ():
    count = 0

    while count < 2:
        print('Par')
        count += 1
        time.sleep(1)
    
    #a = input('Type name:')

def numero_impar (cantidad):
    count = 0
    while count < cantidad:
        print('Impar')
        count += 1
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=numero_par)
    t1.start()

    t2 = threading.Thread(target=numero_impar, args=(2,)) # En args como es una tupla debemos poner una coma auenque sea un único arumento
    t2.start()