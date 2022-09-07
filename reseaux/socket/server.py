import socket
import threading
import time


# connection multiple
import time


class ThreadForClient(threading.Thread):

    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        # c'est la connection ( conn) qui recoit
        data = self.conn.recv(1024)
        #mots = self.conn.recv(1024)
        # decoder l'information recue
        data = data.decode("utf8")
        #mots = mots.decode("utf8")
        print(data)
        #print(mots)



# ------------------------------------------------------------------------


# adresse et port
# le serveur va écouter sur le 5566
host, port = ('', 5566)

# creer le socket qui sert pour la communication
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((host, port))
print("Le serveur est démaré !")

# faire ecouter le serveur sur le port
while True:
    # mettre en ecoute
    """
    le parametre 5 n'est pas obligatoire, ce paramettre correspond au
    nombre de connection qui peuvent echouer avant que le serveur 
    refuse les connections. le serveur autorisera 5 echec de connection avant
    de refuser des connection supplémentaire
    dans le ces ou le paramettre n'est pas préciser python 3. choisit une valeur
    """
    socket.listen(5)
    # accepter les connections
    conn, address = socket.accept()
    print("Un client vient de se connecté !")

    my_thread = ThreadForClient(conn)
    my_thread.start()


conn.close()
socket.close()
