# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:25:20 2021

@author: Iudhael ADIKPETO
"""

"""
        Modularité
"""
"""
    importer un module premiere maniere
"""
import math 

raccine = math.sqrt(100)
print("raccine carré de 100=",raccine)

print("\n\tdeuxieme maniere")

"""
    importer un module deuxieme maniere
"""
from math import sqrt

raccine = math.sqrt(25)
print("raccine carré de 25=",raccine)

print("\n\ttroisieme maniere")

"""
    importer un module troisieme maniere
    importer toute les fonctions de la bibliothèque
"""
from math import *

raccine = math.sqrt(4)
print("raccine carré de 4=",raccine)

"""
import os
os.system("cls")
"""

"""
            exemple
"""
import includes.module1
n3=input("un entier?\n\t:")
n3=int(n3)

n4=input("un entier?\n\t:")
n4=int(n4)
print("Somme de {} et de {} égale".format(n3, n4),includes.module1.addition(n3, n4))


import includes.module1 as module1
n3=input("un entier?\n\t:")
n3=int(n3)

n4=input("un entier?\n\t:")
n4=int(n4)
print("Somme de {} et de {} égale".format(n3, n4),module1.addition(n3, n4))
















