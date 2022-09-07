# creer une liste

"""
    methode 1
inventaire = list() # liste vide


    methode 2
    inventaire = [] liste vide
"""

inventaire = [1, 6, 15, "voiture"] # non vide
print(inventaire)
print("\n")

# avec un certain nombre d'élement au debut
inventaire = [0, "arc"] * 5
print(inventaire)

"""
liste avec un certain nombre de valeur croissante
inserre de 0 a 19 dans la liste 
"""

inventaire = range(10)
print(inventaire)
# afficher le contenue de cette liste
for valeur in inventaire:
    print(valeur)
"""
for i in range(0,10):
    print(inventaire[i])
    
    ou
    
i = 0
while i < len(inventaire):
    print(inventaire[i])
    i += 1

    ou 
"""

inventaire = ["arc", "épée", "bouclier", "potion", "flèche", "tunique"]
print(inventaire[:]) #les : pour afficher tous les elements


print("affiche l'element d'indice 2 en partant du debut")
print(inventaire[2])

print("affiche l'element d'indice 2 en partant de la fin")
print(inventaire[-2])


print("afficher les 2 premiers elements")
print(inventaire[:2])

print("afficher les 2 derniers  elements")
print(inventaire[3:])

print("afficher l'indice  2 à l'element d'indice 4-1 = 3")
print(inventaire[2:4])
print("\n")

# modifier la liste
inventaire = ["arc", "épée", "bouclier", "potion"]
print(inventaire[:])
print("Modification de l'element d'indice 2")
inventaire[2] = "bouclier d'acier"
print(inventaire[:])
print("\n")

inventaire = ["arc", "épée", "bouclier", "potion"]
print("Modification des 2 premiers elements")
inventaire[:2] = ["bouclier d'acier","bouclier d'acier"]
# ou inventaire[:2] = ["bouclier d'acier"] * 2
print(inventaire[:])
print("\n")

 # modifier tous les elements
inventaire[:] = ["bouclier d'acier"] * 4
print(inventaire[:])


inventaire = ["arc", "épée", "bouclier", "potion"]
print(inventaire[:])
if "bouclier" in inventaire:
    print("j'ai un bouclier")
else:
    print("pas de bouclier")
print("\n")

# " append "pour ajouter un element a la liste
print("\nnew liste vide")
inventaire = []
print(inventaire[:])

inventaire.append("Arc") # " append "pour ajouter un element a la liste
inventaire.append("bouclier")
inventaire.append("Manteau de cuir ")
print(inventaire[:])

print("inserer un element en indice 1 avec ' assert '")
inventaire.insert(1, "Potion de mana")
print(inventaire[:])


print("supprimer des elements")
inventaire.remove("bouclier")
"""
 ou > del inventaire[1]
"""
print(inventaire[:])
print("\n")

# trouver l'indice d'un element de la liste
print("Indice de l'element Potion de mana : ", inventaire.index("Potion de mana"))
print("\n")

# trier une liste avec le mot (des element de meme type) "sort"

inventaire = ["Potion de mana", "Arc", "Bouclier", "Manteau de cuir", "Arbalète"]
print(inventaire)

inventaire.sort()
print(inventaire)

inventaire = [5, 128, -7, 3, 124, 7, -5, 2, -8, 178]
print(inventaire)
print("trie normale")
inventaire.sort()
print(inventaire)
print("renverser la liste avec le mot reverse")
inventaire = [5, 128, -7, 3, 124, 7, -5, 2, -8, 178]
inventaire.reverse()
print(inventaire)

print("\n")
# compter le nombre de fois qu'on a un element dans une liste
inventaire = ["Potion de mana","Potion", "Arc", "Bouclier","Potion", "Manteau de cuir", "Arbalète"]
print(inventaire)
print("Nombre de potion : ", inventaire.count("Potion"))

print("\n")
print( "supprimer tous les element de la liste avec clear")
inventaire.clear()
# ou inventaire = []
print(inventaire)

print("\n")
print("passer d'une liste a une chaine")
inventaire = ["Bonjour", "à", "tous"]
print(inventaire)
phrase = "-".join(inventaire) # le separateur est un tiret
print(phrase)

print("\n")

print("copie d'une liste")

liste1 = ["Arc", "tunique"]
# ne permet pas la copie de lisye 1 dans liste 2 mais ajoute un element dans chaque liste
liste2 = liste1
print("liste 1", liste1)
print("liste 2", liste2)

liste2.append("Bouclier")

print("liste 1", liste1)
print("liste 2", liste2)

print("\n")
print("pour reussir la copie on import le module copy")
import  copy

liste2 = copy.deepcopy(liste1)
print("liste 1", liste1)
print("liste 2", liste2)

liste2.append("Bouclier")

print("liste 1", liste1)
print("liste 2", liste2)

print("\n")
print("concatener deux liste")
liste2 = ["parchemin", "potion"]
print(liste1)

liste1.extend(liste2)
# ou liste1 = liste1 + liste2 ou liste1 += liste2
print(liste1)

print("\n")
print("Parcourir une liste")
for objet in liste1:
    print(objet)
print("\n")
for objet in enumerate(liste1):
    print(objet) # enumerate affiche l'indice et la valeur

print("\n")
for indice_objet, valeur_objet in enumerate(liste1):
    # recuperation l'indice et la  valeur
    print("element d'indice {} -> {}".format(indice_objet, valeur_objet))

