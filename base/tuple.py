"""
tuple : conteneur de type sequence (les listes aussi)
un tuple, une fois creer ne peut etre modifier, peut servir a definir des constantes
"""


"""

# creer un tuple   mon_tuple = () # tuple vide
                   print(type(mon_tuple))
        
        si le tuple ne contient qu'une seule valeur ajouter la vigule
                    mon_tuple = (45,)
                    mon_tuple = 45,
                    mon_tuple = (4, 6) # plusieurs valeurs
  
accès aux valeurs : mon_tuple[X]        # valeur d'indice X

on peut retouner un tuple a une fonction plutot qu'une valeur (retour multipl)
"""
mon_tuple = (45, 64)

print(mon_tuple)
print("premier indice du tuple")
print(mon_tuple[1])

print("\n")
# dans le caas d'une affectation multiple on peut modifier les variables
(nbr1, nbr2) = (14, 46)
print(nbr1, nbr2)

print("\n")
# retour multiple
def get_player_position(posX = 148,posY = 86):
    return (posX, posY)

# programe principale
coordx, coordy = 0, 0

print("Position du joueur : ({}/{})".format(coordx, coordy))

(coordx, coordy) = get_player_position()

print("Position du joueur : ({}/{})".format(coordx, coordy))

# affectation multiple
coordx = 15
coordy = 18

print("Position du joueur : ({}/{})".format(coordx, coordy))








