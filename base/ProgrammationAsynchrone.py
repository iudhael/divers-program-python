import time

import threading



def process_one():
    i = 0
    while i < 3:
        print("ooooooooooo")
        time.sleep(0.3)
        i += 1


def process_two():
    i = 0
    while i < 3:
        print("xxxxxxxxxxxxx")
        time.sleep(0.3)
        i += 1

# execution en paralelle des fonction
th1 = threading.Thread(target=process_one)

th2 = threading.Thread(target=process_two)

# demarrer
th1.start()
th2.start()

# permettre que chaque tread attendent  la fin de l'un de l'autre avant de continué
# le programme sequentielle

th1.join()
th2.join()

print("Fin du programme...")




class MyProcess(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        i = 0
        while i < 3:
            print(threading.currentThread())
            time.sleep(0.3)
            i += 1




th1 = MyProcess()

th2 = MyProcess()

# demarrer
th1.start()
th2.start()


th1.join()
th2.join()

print("Fin du programme...")





# bloquer l'operation de sorte a l'aisser un processus se terminer d'abord
# LE PROCESSUS EST TOUJOUR EN PARRALELLE


    # creer un verrou
my_lock = threading.RLock()

class MyProcess(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        i = 0
        while i < 3:
            with my_lock:
                letters = "ABC"
                for lt in letters:
                    print(lt)
                    time.sleep(0.3)
            i += 1
# COMME sa on ABC et non des decallage AABBCC...

th1 = MyProcess()

th2 = MyProcess()

# demarrer
th1.start()
th2.start()


th1.join()
th2.join()

print("Fin du programme...")













