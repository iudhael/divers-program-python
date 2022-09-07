import socket
import threading



# ------------------------------------------------------------------------


# adresse et port
# le serveur va écouter sur le 5566
host, port = ('127.0.0.1', 55555)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
print("Le serveur est démaré !")

# faire ecouter le serveur sur le port
server.listen()

clients = []
nicknames = []

# envoie un message a tous les clients connectés
def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # apres l'envoi du message on obtient l'index du client et on le supprime pour mettre fin a la fonction
            index = clients.index(client)
            clients.remove(client)
            client.close() # fermer la connection au client
            # donner le surnom du client
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode('ascii')) # envoyer un message pour dire que quelqu'un a quitté le chat
            nicknames.remove(nickname)
            break

def receive():
    while True:
        # accepter les connections
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii')) # le client envoi son pseudo au serveur
        nickname = client.recv(1024).decode('ascii')
        clients.append(client)

        # afficher le pseudo du client
        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('ascii')) # informer les autre clients qu'il y a une connection
        client.send('connected to the server!'.encode('ascii'))

        # gerer l'envoi des message de touts les client en meme temps
        thread = threading.Thread(target=handle,    args=(client,))
        thread.start()

print("Le serveur est en écoute...")
receive()

