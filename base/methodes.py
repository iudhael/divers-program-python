# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:44:25 2021

@author: Iudhael ADIKPETO
"""

"""
    Methodes
"""

# créer une classe Humain
class Humain:
    
    """
    attribut de class
    """
    lieu_habitation = "Terre"
    
    def __init__(self,nom, age):
        
        self.nom = nom
        self.age = age
    
    
    """
    une methode est une fonction sur une instance
    création d'une methode standar qui fonctionne 
    uniquement sur un objet
    
    "self" est pour une methode standare
    """
    
    def parler(self, message):
        print("{} a dit : {}".format(self.nom, message))
     
    """
    Methode de classe methode qui a directement un
    impact sur la classe "Humain"
    permet de changer un attribut de classe
    
    "cls" (classe)pour une methode de classe 
    """
    #creation méthode de classe
    def changer_planete(cls, new_planete):
        Humain.lieu_habitation = new_planete
        
    planete = classmethod(changer_planete)
    #fin de la création de methode de classe
    
    """
    Création d'une méthode statique
    cette methode est lier a la classe mais indépendante 
    peut etre appeler n'importe comment non lier à
    un objet ni une class
    """
    
    def definition():
        print("L'Humain est classé au sommé de la chaine alimentaire")
    definir = staticmethod(definition)    
        
        
        
# programme principal
print("L'ancement du programme...")

#appel methode statique
Humain.definir()

#fin appel

h1 = Humain("iud", 18)
"""
print("Prénom de h1 : {}".format(h1.nom))
print("Age de h1 : {} ans.".format(h1.age))
"""
#appel methode standar
h1.parler("Bonjour à tous ! :)")
h1.parler("Comment allez-vous ?")

#fin appel

#appel methode de classe
print("Planete actuelle {}".format(Humain.lieu_habitation ))

Humain.planete("Mars")

print("Planete actuelle {}".format(Humain.lieu_habitation ))


#fin appel





 