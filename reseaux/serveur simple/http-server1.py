# établir un serveur HTTP

import http.server
import socketserver




"""
utliser python comme langage coté serveur à la place du php

et html et css pour le coter client

"""

# INITIALISER UN PORT
    # le port http est initialiser sur le port 80

port = 80
    # definir une address l'endroit ou on veut se connecter
    # ici on est en local pas besoin de mettre locajhost aussi
address = ("", port)

    # Mettre en place le gestionneur : pour erer les requette http
handler = http.server.SimpleHTTPRequestHandler
    # preparer le serveu
httpd = socketserver.TCPServer(address, handler)

print(f"Serveur demmarré sur le PORT {port}")

    # deservir le serveur (le quitter)
httpd.serve_forever()

"""
pour demarer le serveur aller dans l'invite de commande dans 
le dossier contenat le fichier et taper 'python .\http-server.py'

tant que la console est ouverte le serveur tourne

"""


