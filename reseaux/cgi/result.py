"""
    données formulaire
ce fochier recois les données d'un formulaire

meme methode pour les autre champs d'un formulaire

on peut associer des pages html avec des script python on peut aussi utiliser
du java script ici
"""
import cgi
# ce module traite les données de formulaire c'est un gestionnaire pour cgi
import cgitb

"""
la ligne suivante n'est utiliser qu'en developpemet 
l'enlever ou le mettre en commentaire lorsque le site est en ligne

    Activation du mode debuggue
"""

cgitb.enable()

# recuperation des données par la creation d'un form
form = cgi.FieldStorage()

# toujours filtrer les champs de formulaire
# verifier si le champs 'username' existe


    # definir l'entete
print("Content-type: text/html; charset=utf-8\n")

html = """ <!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
    <h1>Page de resultat</h1>
"""
print(html)


try:
    if form.getvalue("username"):
        # si le champs existe
        username = form.getvalue("username")
        print(f"<p>Bonjour {username} !</p>")

        # print("<script>alert('ok')</script>")

    else:
        raise Exception("Pseudo non transmis")
except:
    print("<p>Pseudo non transmis</>")




html = """

</body>
</html>
"""

print(html)


















