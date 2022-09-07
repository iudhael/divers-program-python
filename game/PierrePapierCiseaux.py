# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 13:36:21 2021

@author: Iudhael ADIKPETO
"""

"""
Pierre Papier Ciseaux
"""
from random import randrange
from time import sleep



while True:
    reponse = randrange(1,4)
    print("Pirre, Papier, Ciseaux ???")
    print("1=> Pirre\n2=>Papier\n3=>Ciseaux\nChoisissez un chiffre entre 1 et 3")
    while True:
        R = input("\t: ")
        R = int(R)
        if R <= 0 :
            print("Réessaie un autre chiffre!!!")
        elif R >= 4:
            print("Réessaie un autre chiffre!!!")
        
        else:
            print("ok!!!")
            break 
    sleep(3)
    if reponse == 1:
        print("Pierre")
    elif reponse == 2:
        print("Papier")
    else:
        print("Ciseaux")
    if reponse == R:
        print("Gagner!!!")
    else:
        print("Perdu!!!")
    
    print("Voulez-vous quitter le jeu oui ou non ?")
    sortir = input("\t:")
    if sortir == "oui":
        print("Fin du programme...")
        break
    
    