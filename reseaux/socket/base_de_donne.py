import sqlite3

# toujours gérer les erreurs
try:
    # se connecter au fichier de base de donnée
    connection = sqlite3.connect("base_donne.db")


    cursor = connection.cursor()
    """
    my_username = ("judicael",) # tuple
    req = cursor.execute('SELECT * FROM iud_users WHERE user_name = ?', my_username)

    result = cursor.fetchone()[2]
    print(f"Le nom de l'utilisateur est :{result}")
    """


    # recuperer les modifications en les affichant
    requ = cursor.execute('SELECT * FROM iud_users')
    # print(requ.fetchall())

    # parcourir l'information
    for row in requ.fetchall():
        print(row[2])
        # pour afficher l'indice 1 uniquement faire 'print(row[1])'



except Exception as e:
    print("[ERREUR] ", e)
    # revenir au dernier commit si il y a une erreur
    connection.rollback()









finally:
    # fermer la base de donnée a la fin
    connection.close()















