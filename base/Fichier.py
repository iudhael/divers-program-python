"""
Mode d'ouverture :  r (lecture seule)
                    w (l'ecriture avec remplacement)
                    a (ecriture avec ajouit en fin de fichier)
                    x (lecture et ecriture)
                    r+ (lecture/ecriture dans un meme fichier)

lecture         :   read(), readline(), readlines()
ecriture        : write()

"""


print("Premiere methode d'ouverture")
fic = open("docs/donnees.txt", "r")


# recuperer l'ensemble du fichier
content = fic.read()
print(content)

"""
# recuperer une ligne du fichier
line = fic.readline()
print(line)

line = fic.readline()
print(line)

# readlines  permet de recuperer le reste des lignes
line = fic.readlines()
print(line)
"""
fic.close()

# verifier si le fichier a ete bien fermer
if fic.closed:
    print("fichier fermer")
else:
    print("fichier toujours ouvert")

print("\n")

print("deuxieme  methode d'ouverture")

with open("docs/donnees.txt", "r") as fic:
    content = fic.read()
    print(content)

    # pas besoin d'utiliser 'close()' pour fermer le fichier avec 'whith'

print("\n")

print("Ecriture en fichier texte on change de mode")
with open("docs/data.txt", "w") as fic:
    nombre = 15
    fic.write(str(nombre))
    fic.write("\nBonjour, je suis une phrase\n")
    fic.write("Et une autre...\n")

print("\n")
print("enregistrer tout l'objet en mode binaire dans un fichier texte")

import pickle

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def whoami(self):
        print("{} ({})".format(self.name, self.level))

"""
sauvegarde
p1 = Player("judi", 18)

# ajouter un b pour le mode binaire
with open("docs/player.data", "wb") as fic:
    record = pickle.Pickler(fic)
    record.dump(p1)
"""
# recuperation des information depuis le fichier en binaire : on change de mode
with open("docs/player.data", "rb") as fic:
    get_record = pickle.Unpickler(fic)
    player_one = get_record.load()

player_one.whoami()
