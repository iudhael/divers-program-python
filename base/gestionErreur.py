# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:50:39 2021

@author: Iudhael ADIKPETO
"""

ageUtilisateur = input("Quel est votre age ? ")

"""
pour eviter l'erreur qui s'affiche losqu'on tape 
une valeur differente d'un entier "ValueError" on 
peut procéder comme suit

le else s'execcute uniquement en cas de valeur correcte ou de 
réussite
le finally s'execcute dans tous les cas

"""

try:
    ageUtilisateur = int(ageUtilisateur)
except:
    print("L'age indiqué est incorrecte !!!")

else:
    print("Tu as", ageUtilisateur ,"ans." )

finally:
     print("Fin du programme..." )
     

"""
    gerer plusieur erreurs
"""
n1 = input("Choisissez un entier pour la division: ")

n2 = input("Choisissez un autre entier pour la division: ")

try:
    n1 = int(n1)
    n2 = int(n2)
    print("La division de {} et de {} donne {}.".format(n1, n2, n1 / n2))
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser {} par zéro.".format(n1))

except ValueError:
    print("Vous devez entrer un nombre.")
    
# pour prendre en compte d'autre erreurs     
  
except:
    print("Valeur incorrecte.")

else:
    print("Bravo !!!" )
    
finally:
     print("Fin du programme..." )

"""
AssertionError
"""
try:
    age = input("Quel age as-tu ? ")
    age = int(age)
    
    assert age >= 18 #je veux que age soit plus grand ou = à 18
except AssertionError:
    print("J'ai eu une exception!!\n\tL'age entré est plus petit que 18.")
else:
    print("Bravo!!!\n\tVous etes majeur!!!" )
finally:
     print("Fin du programme..." )



