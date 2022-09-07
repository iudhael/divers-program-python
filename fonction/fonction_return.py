# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:28:25 2021

@author: Iudhael ADIKPETO
"""

"""
    Fonction qui retourne quelque chose
"""

def addition(n1, n2):
    resultat = n1 + n2
    return resultat

print(addition(5, 2))

# ou

def addition(n1, n2):
   return n1 + n2
n3=input("un entier?\n\t:")
n3=int(n3)

n4=input("un entier?\n\t:")
n4=int(n4)
print("Somme de {} et de {} égale".format(n3, n4),addition(n3, n4))



"""
            comparer des nombres
            plusieurs return
"""
print("Comparaison")

def max(n1, n2):
    if n1 < n2:
        return n2
    elif n1>n2:
        return n1
    else:
        return "egalite!!!"
    
n3=input("un entier?\n\t:")
n3=int(n3)

n4=input("un entier?\n\t:")
n4=int(n4)
print("Le plus grand entre {} et  {} est".format(n3, n4),max(n3, n4))


"""
foction permettant d'indiquer si un nombre est paire ou non
"""
def paire():
    nbre = input("Saisissez un nombre :")
    nbre = int(nbre)
    if nbre % 2 == 0:
        return print("Paire.")
    else:
        return  print("Impaire.")
if __name__ == "__main__" :
    print("Phase de test")
    paire()



















