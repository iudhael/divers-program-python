# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 17:24:54 2021

@author: Iudhael ADIKPETO
"""

"""
fonction sans parametre
"""

def bonjour():
    print("hello world!")
    
#on sort de la fonction
    
#Exécution de la fonction
    
bonjour()


# nouvelle fonction 
# fonction avec parametre

def dire(nom="Vous", message="Bonjour"):
    print("{} : {}".format(nom, message))

#on sort de la fonction
    
# Exécution 
    
dire("judi", "salut")

"""
on peut affecter des valeurs par défaut aux variables de la fonction
ce qui permet d"afficher cette valeur lorsque la fonction est appelée mais 
en précisant un seul parametre alors qu'elle en demande 2
"""
#   exemple

dire()
dire("Sali")

print("\n")

""" 
foction avec des parametres infinis
"""
def nom_inventaire(*listNom):
    for nom in listNom:
        print(nom)
    
"""
    Grace a l'etoile et a la boucle for on fais des parametres infini
""" 
# on sort de la fonction
    
nom_inventaire("judi")
nom_inventaire("judicael", "sali", "iud hael", "buzz l'éclaire", "mick")
















