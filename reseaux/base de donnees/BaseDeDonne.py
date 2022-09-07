"""
base de données
    pour remplacer le stockage par les fichiers texte
    stocker des information de maniere relationnelle
    stocker sous forme de table
    creer des relation entre les table

Systeme de gestion de base de données ou LGBT : MySQL,SQLite, ...
Aucune des bases de données n'est plus mieux que l'autre tout dépend de
de notre projet
            SQlite :    concu  pour  mobile
                        les données doivent etre < au Giga-octet, dans le cas
                        contraire ne pas l'utiliser
                        multiple connection --> si la base de données doit
                        etre utiliser par plusieurs utilisateurs ne par l'utiliser


            MySQL : une solution pour SQLite, utiliser pour les forums, news

            PostgreSQL :    plus performant que mySQL sur de tres grand base
                            de donné
                            manipule des bases de données de plusieurs Tera-octet
                            de données (un CHU , tout un service medicale

"""
# SQLite
# creer les tables via le logiciel browser for SQLlite

import sqlite3

# toujours gérer les erreurs
try:
    # se connecter au fichier de base de donnée

    connection = sqlite3.connect("base.db")

    """
    quand on manipule une base de donnée il faut faire ces 4 elemennts
     CRUD : Create, Read, Update, Delete
    """

    # creer le curseur qui permet de travailler avec les requettes

    cursor = connection.cursor()

    # lire les infos de la base de donné
        # l'etoile pour dire je selectionne tout
    """
    tu selectionne toutes les info depuis la base de donner iud_users dans le cas ou
    le champ user_name est egal a judicael
    """
    """
    my_username = ("judicael",) # tuple
    req = cursor.execute('SELECT * FROM iud_users WHERE user_name = ?', my_username)
    """
    # afficher l'information
    """
    'fetchone' car on veut faire afficher qu'un seul elemnt 
    dans le cas de plusieurs elment utiliser 'fetchall'
    """

    # affiche la totalité des info sur l'utilisateur --> print(cursor.fetchone())
        # recuperer l'indice 1 l'indice 0 est l'identifiant de l'indice 1
    """
    result = cursor.fetchone()[1]
    print(f"Le nom de l'utilisateur est :{result}")
    """


    # eregistrer un aute element
    """
    l'identifiant est généré par la base avec cursor.lastrowid
    on passe uniquement le nom et le level
    
    """
    """
    new_user = (cursor.lastrowid, "julien", 24)
    
    # requette pour enregistrer un nouvelle element
    cursor.execute('INSERT INTO iud_users VALUES(?, ?, ?)', new_user)
    # valider les mdifications sur la base pas la connection
    connection.commit()
    print("Nouvelle utilisateur ajouter !")
    """

    # eregistrer plusieurs elemnets d'un coups avec executemany
    """
    new_user1 = [(cursor.lastrowid, "naruto", 18), (cursor.lastrowid, "sasuké", 18)]
    cursor.executemany('INSERT INTO iud_users VALUES(?, ?, ?)', new_user1)
    
    # valider les mdifications sur la base pas la connection
    connection.commit()
    print("Nouvelle utilisateur ajouter !")
    
    """

    # recuperer les modifications en les affichant
    requ = cursor.execute('SELECT * FROM iud_users')
    # print(requ.fetchall())

    # parcourir l'information
    for row in requ.fetchall():
        print(row)
        # pour afficher l'indice 1 uniquement faire 'print(row[1])'



except Exception as e:
    print("[ERREUR] ", e)
    # revenir au dernier commit si il y a une erreur
    connection.rollback()









finally:
    # fermer la base de donnée a la fin
    connection.close()















