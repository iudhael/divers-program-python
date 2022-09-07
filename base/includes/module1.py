# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 21:11:54 2021

@author: Iudhael ADIKPETO
"""
"""
        module 
        pour ouvrir ce module depuis un fichier en dehors du dossier includes
        on tape dans le fichiers :
            import includes.module1
                #appelle d'une fonction de module1
            include.module1.nomFonction()
            
                    ou
                    
            import includes.module1 as module1
             #appelle d'une fonction de module
            module1.nomFonction()
"""


def addition(n1, n2):
   return n1 + n2

if __name__ == "__main__" :
    print("phase de test")
    n3=input("un entier?\n\t:")
    n3=int(n3)
    n4=input("un entier?\n\t:")
    n4=int(n4)
    print("Somme de {} et de {} égale".format(n3, n4),addition(n3, n4))
    

