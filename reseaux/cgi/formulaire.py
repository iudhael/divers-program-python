# coding:utf-8
import cgi


# definir l'entete format ---> ( nom de l'entete: type; valeur)
print("Content-type: text/html; charset=utf-8\n")

html = """ <!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
    <h1>Page web avec python CGI</h1>

    <h2>Formulaire</h2>

    <form method="post" action="result.py">
        <p>
            <input type="text" name="username"/>
            <input type="submit" value="Envoyer"/>
        </p>

</body>
</html>
"""

print(html)

