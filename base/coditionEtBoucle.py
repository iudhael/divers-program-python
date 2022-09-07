# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:44:25 2021

@author: Iudhael ADIKPETO
"""
a=input("entrer une lettre ")

if a in "aeiouy":
    print("c'est une voyelle")
else:
    print("c'est une consonne ")
    
    
a=input("entrer une lettre")

if a not in "aeiouy":
    print("c'est une consonne")
else:
    print("c'est une voyelle ")
    
a=input("entrer votre age ")
a=int(a)

if a<18:
    print("mineur")
elif a==18:
    print("majeur")
elif a>18 and a<25 :
    print("vous etes jeune")
else:
    print("vous avez", a,"ans")
    
a=input("entrer votre age ")
a=int(a)



b=input("True or False ")
if b:
    print("c'est vrai")
else:
    print("c'est faux")
  
"""
boucle while et for
"""
# while
x = 0
while x < 5:
    print("x = ",x)
    x +=1

# for
for letter in "coucou":
    print(letter)
    #ou
salut = "bonjour"
for letter in salut:
    print(letter)

# for
"""
range contient la valeur initile et une valeur de fin qui n'est 
pas comprise
"""
for i in range(0,10):
    print("x = ",i)

#ou
"""
range contient la valeur initile  une valeur de fin qui n'est 
pas comprise et le pas qui est 2 ici
"""
for i in range(0,11,2):
    print("x = ",i)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



