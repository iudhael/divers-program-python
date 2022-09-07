"""
Mode TCP    : etablit une connection une bonne fois pour toute comme un appel, on
              s'assure que les informations sont bien recues

Mode UDP    : mode non connecter, plus rapide,on ne sassure pas que les informations
              sont bien recuees, comme dans les jeux en ligne

"""
"""
communiquer avec nos programme au sein du reseaux local (exemple : notre ordi)

"""

import socket
import sqlite3

# on peut ecrire 127.0.0.1 a la place de localhost
host, port = ('localhost', 5566)

# creer un socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # se connecter au fichier de base de donnée
    connection = sqlite3.connect("base_donne.db")

    cursor = connection.cursor()

    requ = cursor.execute('SELECT * FROM iud_users')

    print("Saisissez votre identifiant puis votre mot de passe")
    identifiant = input("Saisissez identifiant : ")
    mot_pass = input("Saisissez mot de passe : ")

    i = 0

    #for row in requ.fetchall():
     #   print(row[1].find(identifiant))

    id = ""
    passe = ""
    for row in requ.fetchall():
        if identifiant == row[1] and mot_pass == row[2]:
            id = identifiant
            passe = mot_pass
            print(id)
            print(passe)
        """
        else:
            if mot_pass not in row[2]:
                print("mot non trouve")
            elif identifiant not in row[1]:
                print("id non trouve")
        """
    for row in requ.fetchall():
        if identifiant != row[1] and mot_pass != row[2]:
            while id != row[1] and passe != row[2]:
                print("identifiant ou passe incorrecte")
                print("Saisissez votre identifiant puis votre mot de passe")
                identifiant = input("Saisissez identifiant : ")
                mot_pass = input("Saisissez mot de passe : ")

                if identifiant == row[1] and mot_pass == row[2]:
                    id = identifiant
                    passe = mot_pass
                    print(id)
                    print(passe)




    # connecter le client au serveur
    socket.connect((host, port))
    print("Client connecté !")

    # encoder l'information avant l"envoi au serveur qui se chargera de la décodée

    data = input("Bonjour !\n Quel est votre requette ?\n\t :")
    # mots = "Bye !"
    mot = input("Tapez exactement le mot 'bye' pour sortir : ")

    while mot != "bye":
        data = input("Bonjour !\n Quel est votre requette ?\n\t :")
        mot = input("Tapez exactement le mot 'bye' pour sortir : ")

    # ender l'information
    data = data.encode("utf8")
    # mots = mots.encode("utf8")
    # envoyer la données
    socket.sendall(data)
    # socket.sendall(mots)





except ConnectionRefusedError:
    print("Connexion au serveur échouée !")
finally:
    socket.close()
