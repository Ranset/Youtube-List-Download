import threading
import time
import multiprocessing

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
        #print('Impar')
        print(count)
        count += 1
        time.sleep(1)


if __name__ == "__main__":
    # t1 = threading.Thread(target=numero_par)
    # t1.start()

    # t2 = threading.Thread(target=numero_impar, args=(2,)) # En args como es una tupla debemos poner una coma auenque sea un único arumento
    # t2.start()

    t3 = multiprocessing.Process(target=numero_impar, args=(50,), daemon=True)
    t3.start()
    t4 = multiprocessing.Process(target=numero_impar, args=(50,), daemon=True)
    t4.start()
    
    time.sleep(6)
    t3.terminate()
    time.sleep(5)
    t4.terminate()