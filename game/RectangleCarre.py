class Rectangle:

    def __init__(self, L = 0, l = 0):
        self.nom = "Rectangle"
        self.L = L
        self.l = l

    def mesure(self):

        print("Bonjour !!!\nVoulez-vous calculer:")
        print("\t1)le périmetre ?")
        print("\t2)la surface ?")
        print("\t3)le perimetre et la surface ?")

        n = input("Choisissez un numéro :")
        n = int(n)

        while n < 1 or n > 3:
            n = input("Choisissez un numéro entre 1 et 3 :")
            n = int(n)
        if n == 1:
            """
            print("Tapez la premiere dimension de votre {}. ".format(self.nom))
            self.L = float( input("\t:") )
            print("Tapez la seconde dimension de votre {}. ".format(self.nom))
            self.l = float( input("\t:") )
            """

            return (self.L + self.l) * 2
        elif n == 2:
            """
            print("Tapez la premiere dimension de votre {}. ".format(self.nom))
            self.L = float(input("\t:"))
            print("Tapez la seconde dimension de votre {}. ".format(self.nom))
            self.l = float(input("\t:"))
            """

            return self.L * self.l
        elif n == 3:
            """
            print("Tapez la premiere dimension de votre {}. ".format(self.nom))
            self.L = float(input("\t:"))
            
            print("Tapez la seconde dimension de votre {}. ".format(self.nom))
            self.l = float(input("\t:"))
            """
            print("Perimetre = {}\nSurface = {} ".format((self.L + self.l) * 2, self.L * self.l))

class Carre(Rectangle):

    def __init__(self, c ):
        Rectangle.__init__(self, c, c)
        self.nom = "Carré"



if __name__ == "__main__" :

    r = Rectangle(8, 4).mesure()
    print(r)

    r = Carre(3).mesure()
    print(r)
