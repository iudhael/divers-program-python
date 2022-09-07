#coding:utf-8
import  cgi



# ces 2 modules permettront de gerer  les accents, defauts d'affichages
import sys
import codecs
    # remodifier l'encodage pour la sortie stadard
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())





    # definir l'entete format ---> ( nom de l'entete: type; valeur)
print("Content-type: text/html; charset=utf-8\n")


html = """ <!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
    <h1>Page web <a href ="formulaire.py">avec</a> python CGI</h1>
    <h2><a href ="formulaire.py">Formulaire</a></h2>
    <h2><a href ="cookie.py">Cookie</a></h2>
    <h2><a href ="#">Base de données</a></h2>
</body>
</html>
"""



print(html)










