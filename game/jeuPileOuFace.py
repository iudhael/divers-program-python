# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 12:17:24 2021

@author: Iudhael ADIKPETO
"""

"""
pile ou face
"""
from random import randrange
from time import sleep


while True:
    reponse = randrange(1,3)

    print("Pile ou Face ???")
    print("1=> Pile\n2=>Face\nChoisissez un chiffre entre 1 et 2")

    while True:
        R = input("\t: ")
        R = int(R)
        if R <= 0 :
            print("Réessaie un autre chiffre!!!")
        elif R >= 3:
            print("Réessaie un autre chiffre!!!")
        
        else:
            print("ok!!!")
            break 
        
    sleep(3)
    if reponse == 1:
        print("Pile")
    else:
        print("Face")
    if reponse == R:
        print("\tGagner!!!")
    else:
        print("Désollé!!!")
  
    
    
    print("Voulez-vous quitter le jeu oui ou non ?")
    print("Tapez exactement le mot 'oui' ou le mot 'non' ")
    sortir = input("\t:")
    
    
    if sortir == "non":
        print("On continue")   
    if sortir == "oui":
        print("Fin du programme...")
        break
        
    
        
            
        
        
        
  
        
    
    
    
    

    
