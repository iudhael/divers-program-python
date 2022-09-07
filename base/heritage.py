"""
Created on Fri Jul  2 21:10:43 2021

@author: Iudhael ADIKPETO
"""

"""
Héritage
Héritage mulitple : une classe fille herite de plusieurs autres classe meres
    class Lettre(Majuscule, Miniscule):
"""
# classe mere
class Vehicule:

    def __init__(self, nom, quantite_essence):
        self.nom = nom
        self.essence = quantite_essence

    def se_deplacer(self):
        print("la vehicule {} se deplace...".format(self.nom))


# voiture est une sorte de vehicule
class Voiture(Vehicule):

    def __init__(self, nom_voiture, essence, puissance):
        Vehicule.__init__(self, nom_voiture, essence)
        self.puissance = puissance

    # redefinir une methode existante
    def se_deplacer(self):
        print("je roule...")



class Avion(Vehicule):
    def __init__(self, nom, essence, marchandise):
        Vehicule.__init__(self, nom, essence)
        self.marchandise = marchandise
        # redefinir une methode existante

    # redefinir une methode existante
    def se_deplacer(self):
        print("je survole les airs...")

# progame principale
v1 = Voiture("faucon ", 90, 420)
v1.se_deplacer()
print(v1.puissance, "cheveaux")
avi1 = Avion("faucon millenium", 2000, "Missile")
avi1.se_deplacer()
print(avi1.marchandise, "faucon")

"""
verifier comment un objet fait partir d'une classe fille
"""
class Animal:
    def __init__(self, nom):
        self.nom = nom
    def manger(self):
        print(self.nom, "mange...")

class Reptile(Animal):
    def __init__(self, nom, regime_alimentaire):
        Animal.__init__(self, nom)
        self.regime = regime_alimentaire

    def manger(self):
        print("le reptile mange...")


# code principale
lezard = Reptile("Lézard", "Libellule")
lezard.manger()
# isinstance(<objet>, <classe>) : virifier qu'un objet est de la classe indiquée
# on peut avoir "Reptile" a la place d'animale
print(isinstance(lezard, Animal))
if isinstance(lezard, Animal):
    print("Lezard est un animal")

# issubclass(<classe fille>, <classe mere>) : virifier qu'une classe est fille d'une autre
print(issubclass(Reptile, Animal))
if issubclass(Reptile, Animal):
    print("Reptile herite d'animal")











