# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 11:56:52 2021

@author: Iudhael ADIKPETO
"""

"""
Jeu de déclaration d'amour à une fille
la réponse de la fille est générée de facon aléatoire grace 
à la fonction <randrange> appartenant au module 'random'
avec un suspence(un court temps avant la réponse)
grace à la fonction <sleep> du module 'time'
"""

from random import randrange
from time import sleep
"""
randerange génère une réponse aléatoire  entre 0 et 3
""" 
ReponseFille = randrange(0,4)
print("Est-ce que tu m'aimes ?")

"""
time recoit comme parametre le temps d'attente en seconde
"""
sleep(5)
if ReponseFille == 0:
    print("Je ne peut aimer un homme aussi vilain que toi. ahahah!!!")
elif ReponseFille == 2:
    print("Oui, mais je suis en couple.")
elif ReponseFille == 3:
    print("Oui, mais en tant qu'ami.")

else:
    print("Je t'ai aimé depuis le premier jour que je t'ai rencontré.")

print("Fin du programme...")