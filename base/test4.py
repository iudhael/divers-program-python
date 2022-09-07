# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:47:44 2021

@author: Iudhael ADIKPETO
"""
"""
 la fonction type(variable) indique le type de la variable à utiliser dans un print
 
"""
print("Bonjour\n")
print("\tEntrer votre nom : ")  #\t pour la tabulation
nom = input()
print("Mama Miya " + nom)

age=input("saisissez votre age")
anneeNaissance=input("quel est votre année de naissancde?")

print("votrre nom est {} née en {} vous avezz {} ans".format(nom,anneeNaissance,age))    

  #.format(variable1,variable2,vriable)

texte="votre nom est {} née en {} vous avez {} ans"
print(texte.format(nom,anneeNaissance,age))


a=input("Saisissez un entier ")
a=int(a) #caste

b=input("Saisissez un autre nombre ")
b=int(b)

print("a=",a)
print("b=",b)
print("somme=",a+b)
print("saisissezun entier")
c=input()
                    #c=float(c)
print("c=", c)
print("somme a+c=", a+int(c))

boleen=True
print(boleen)
#boleen=int(boleen)
print(int(boleen))


boleen1=False
print(boleen1)
boleen1=int(boleen1)
print(boleen1)




