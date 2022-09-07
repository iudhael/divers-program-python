# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:57:17 2021

@author: Iudhael ADIKPETO
"""

"""
    classe et attribut
"""
"""
#Variable globale
global h_prenom 
global h_age 
"""
# créer une classe Humain
class Humain:
    """
    classe des etres humains
    init : est une méthode et un constructeur 
    self : cible l'objet(h1),et rend l'objet créer
            ce qui est rendu peut etre retrouver
            dans l'objet h1 grace à l'affectation
            h1 = Humain()
    """
    """
    attribut de classe 
    c'est un attribut commun a tous les objets
    il est créer dans la classe directement
    pour son appel on commence par le nom de la 
    class
    """
    
    humain_crees = 0
    
    def __init__(self, c_prenom, c_age):
        print("Création d'un Humain...")
        """
        global h_prenom 
        global h_age 
        h_prenom = input("Donnez un prénom: ")
        h_age  = input("Donnez un age: ")
        c_prenom = h_prenom
        c_age = h_age
        """
        self.prenom = c_prenom
        self.age = c_age
        
        Humain.humain_crees += 1

print("L'ancement du programme...")
"""
créer un objet ou instencier la classe
l'objet sera stocké dans une variable
"""

h1 = Humain("iud", 18)
print("Prénom de h1 : {}".format(h1.prenom))
print("Age de h1 : {} ans.".format(h1.age))
print("Humain existant : {} .".format(Humain.humain_crees))

"""
h1.prenom = input(":")
print("Prénom de h1 : {}".format(h1.prenom))
permet de changer le nom de h1
"""


h2 = Humain("hael", 19)
print("Prénom de h2 : {}".format(h2.prenom))
print("Age de h2 : {} ans.".format(h2.age))
print("Humain existant : {} .".format(Humain.humain_crees))

















    