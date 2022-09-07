"""
creer un dictionaire : dico = {} # vide
                        dico = { clée : valeur, clée : valeur .... }

pas d'ordre dans le dictionnaire
# acceder a un element
    dico = {"prenom":"judi"}
    print(dico["prenom"]) entre crochet le nom de la clé
    dico = {1:"judi"}
    print(dico[ 1 ])

# ajouter et modification un element    : dico [ clée ] = valeur

# suppression       :   dico.pop(clé)
                            # on peut recuperer la valeur supprimer toujours avec pop
                            valeur_supprimer = dico.pop("chien" )
                            print(valeur_supprimer)
                        del dico[clée]
                        dico.clear

# parcourir le dico en affichant les clé
    for key in dico:
        print(key)
        ou
    print(dico.keys())

# parcourir le dico en affichant les valeurs
    for value in dico.values():
        print(value)
        ou
    print(dico.values())

# parcourrir le dico en affichant la clé et la valeur
    for k,v in dico.items():
        print("Clé : {} -> valeur : {}".format(k,v))

# copies de dictionnaire
    dico = {1:11, 2:22}
    dico2 = dico.copy()

"""
dico = {"prenom":"judi", "chien":"ami de l'homme", "chat":"je suis un chat"}
# verifier l'existence d'une clé
if "chien" in dico:
    print("oui")
else:
    print("non")


# parametre nommer
# deux etoile pour le parametre nommé
# une etoile pour des parametres variable
def maFonctionBizarre(**parametres):
    print(parametres)

# on doit oblogatoirement attribuer des noms aux variables pour les parametre nommé
maFonctionBizarre(dico = {"prenom":"judi", "chien":"ami de l'homme", "chat":"je suis un chat"})

maFonctionBizarre(age = 18, nom = "iud")






