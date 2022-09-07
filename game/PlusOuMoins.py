# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:04:07 2021

@author: Iudhael ADIKPETO
"""

"""
Jeu plus ou moins ou Guess the nomber
ce jeu aide le joueur à deviner un nombre avec des indice générer par la machine de facon 
aléatoire
"""
from random import randint
"""
avec 'randint' la deuxieme valeur qui se trouve etre ici
la valeurMax est contenu dans l'intervalle
"""
print("++++++++++++ JEU DE PLUS OU MOINS  ------------")

valeurMax = 1
while True:
    print("Donnez une valeur surpérieure à 1")
    valeurMax = input("\t:")
    valeurMax = int(valeurMax)
    if valeurMax > 1:
        print("ok!!")
        break
    
print("\tJe viens de penser\
à un nombre entre 1 et {}".format(valeurMax))
nbreAleatoire = randint(1,valeurMax)
while True:
    print("Quel est votre valeur ?")
    nbreUser =int( input("\t:"))
    if nbreUser > nbreAleatoire:
        print("Votre nombre est trop grand")
    elif nbreUser < nbreAleatoire:
        print("Votre nombre est trop petit")
    else:
        print("Bingo!!")
        break
