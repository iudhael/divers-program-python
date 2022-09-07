import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)

        except:
            print("Une ERREUR c'est produite")
            # fermer la connection
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}' # le client tape son message
        client.send(message.encode('ascii')) # le client envoi le message avec la touche entrer


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_trhead = threading.Thread(target=write)
write_trhead.start()


# on peut ajouter des kik, ban, emoji










