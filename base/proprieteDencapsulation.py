# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:35:51 2021

@author: Iudhael ADIKPETO
"""

"""
   Propriété D'encapsulation
   propriéte sorte de petite boite qui 
   permet de modifier un attribut,d'accéder a sa 
   documentation...
"""

# créer une classe Humain
class Humain:
    
    def __init__(self, nom, age):
        print("Création d'un humain...")
        self.nom = nom
        """
        si on veut rendre un attribut non accessible
        c'est à dire impossible de les modifier
        depuis le programme principale on met un 
        tiret de 8 devant l'attribut
        """
        self._age = age
    
    """    
    creation d'une propriété
    la propriété est créer dans la classe
    la propriéter  prend des parametres qui ne sont 
    pas obligatoires
    property(<getter>, <setter>, <deleter>, <helper>)
    les getter, setter sont des accesseurs
    """
    
    """
    creation de methodes standare avec un tiret de 
    8 devant le nom
    utilie en cas de plusieurs instructions dans 
    les methodes
    """
    def _getage(self):
       if self._age <= 1:
           #ou => return "{} {}".format(self._age, "an")
           return str(self._age)+" an"
       else:
           return  "{} {}".format(self._age, "ans")
           # ou => return str(self._age)+" ans"
       
    
    def _setage(self, new_age):
        
        """
        cette methode peut etre utile lorsqu'on 
        cré un site web avec python
        elle permetra de verifier dans un formulaire
        si l'adresse mail est corrrecte, la longeur
        d'une chaine...
        """
        
        if new_age < 0:
            self._age = 0
        else:
            self._age = new_age
            
    """
    def _delage(self):

    #permet de supprimer l'attribut avec le mot clé del
    
        del self._age
    """
    
    age = property(_getage, _setage, "Je suis l'age d'un humain")
        
    
    
        
    
#Programme principale     
h1 = Humain("Hael", 18)

#ici age fait reference à la propriété
print(h1.age)
print("{} a {}".format(h1.nom, h1.age))

h1.age = 1

print("new age",h1.age)

"""
del h1.age

print(h1.age)
"""
"""
help(Humain)

help(Humain.age)

"""
print("{} a {}".format(h1.nom, h1.age))


