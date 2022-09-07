import tkinter
#from tkinter import END
import random
import time

print("*************************** Devine ma Capitale ***************************")

pays = ["Nigeria", "Ghana", "Ethiopie", "Algérie", "Madagascar", "Erythrée", "Mali", "République centafricaine",
        "Gambie", "Guinée-Bissau", "Afrique du Sud", "République du Congo", "Burundi", "Guinée", "Egypte"

        ]

#print(len(pays))

capitale = ["Abuja", "Accra", "Addis-Abeba", "Alger", "Antanananarivo", "Asmara", "Bamako", "Bangui", "Banjul",
            "Bissau", "Bloemfontein", "Brazzaville", "Bujumbura", "Conakry", "Le Caire"

            ]
"""
#print(len(capitale))


#print(indice)
#print(pays[indice])
#print(capitale[indice])



essai = 0
essai_max = 0
mauvaise_reponse = 0

while (essai_max, essai) < (4, 2):
    indice = random.randrange(0, len(pays))
    print(f"Quel est la capitale {pays[indice]}")
    print("Tu as 3 minutes!!")
    reponse = input("Tape ta réponse : ")
    print(f"Tu as tapé {reponse}")
    if reponse == capitale[indice]:
        essai += 1
        essai_max += 1
        #print(f"essai = {essai}")
        #print(f"essai_max = {essai_max}")
        print("Bonne réponse !!!")
    else:
        essai_max += 1
        #print(f"essai_max = {essai_max}")
        print("Mauvaise réponse")

    if essai == 0:
        print(f"tu as 0/3 bonne réponse avec {essai_max} essais ")

    elif essai == 1:
        print(f"tu as {essai}/3 bonne réponse avec {essai_max} essais ")
    else:
        print(f"tu as {essai}/3 bonne réponses avec {essai_max} essais ")

"""


#*****************************************************************************************************

def instruction():
    # fenetre supplementaire
    about_window = tkinter.Toplevel(app)
    about_window.title("Instructions")
    # taille minimale fenetre
    about_window.minsize(440, 280)
    lb = tkinter.Label(about_window, text="Bonjour !")
    lb.grid()

def A_propo():
    # fenetre supplementaire
    about_window = tkinter.Toplevel(app)
    about_window.title("A propos")
    # taille minimale fenetre
    about_window.minsize(440, 280)
    lb = tkinter.Label(about_window, text="Bonjour !")
    lb.grid()

def saisi_reponse():
    global resultat, reponse

    reponse = entry_reponse.get()

    reponse = reponse.title()
    reponse = reponse.replace(' ', '')
    print(reponse)
    #entry_reponse.delete(0, tkinter.END)


def resultat_fonc():
    global resultat, reponse
    reponse = entry_reponse.get()
    reponse = reponse.title()
    reponse = reponse.replace(' ', '')
    if reponse == capitale[indice]:
        resultat = tkinter.Label(app, text="Bonne réponse !!!")
        resultat.grid(row=4, pady=50)

    else:
        resultat = tkinter.Label(app, text=f"Désolé !! La bonne réponse est : {capitale[indice]}")
        resultat.grid(row=4, pady=50)




def delete(name):
    name.destroy()




def initialisation():
    global indice, entry_reponse, question, valide_reponse, pays_choose
    question_change()
    reponse_aleatoire()
    #indice = random.randrange(0, len(pays))
    #pays_choose = pays[indice]
    #question = tkinter.Label(app, text=f"Quel est la capitale {pays_choose} ?")
    #question.grid(padx=640/4, pady=10)

    entry_reponse = tkinter.Entry(app, width=25)
    entry_reponse.grid(sticky="w", row=3, padx=200)

    valide_reponse = tkinter.Button(app, text="ok", width=8, command=lambda : [saisi_reponse(), resultat_fonc(), desactive_bouton(valide_reponse, continuer), desactive_bouton(entry_reponse, continuer), score_change(), game_over()])
    valide_reponse.grid(sticky="e", row=3, padx=150)



def suite():
    global continuer
    continuer = tkinter.Button(app, text="Continuer", width=10, height=1, state="disabled", command=lambda: [desactive_bouton(continuer, valide_reponse), question_change1(), change_reponse_aleatoir(), active_entry(), delete(resultat), decompte()])
    continuer.grid(row=5, pady=10)

def question_change():
    global indice, question
    indice = random.randrange(0, len(pays))
    pays_choose = pays[indice]
    #question["text"] = f"Quel est la capitale {pays_choose} ?"

    question = tkinter.Label(app, text=f"Quel est la capitale {pays_choose} ?")
    question.grid(padx=640/4, pady=10)

    print(capitale[indice])

def question_change1():
    global indice
    indice = random.randrange(0, len(pays))
    pays_choose = pays[indice]
    question["text"] = f"Quel est la capitale {pays_choose} ?"



    print(capitale[indice])

def reponse_aleatoire():
    global indice1, indice2, rep1, rep2, rep3, variation
    indice1 = 0
    indice2 = 0
    variation = random.randrange(0, 3)

    #while indice1 == indice2 or indice1 == indice:
    if indice1 == indice2 or indice1 == indice :
        indice1 = random.randrange(0, len(capitale))
        indice2 = random.randrange(0, len(capitale))

    if variation == 0:
        rep1 = tkinter.Label(app, text=f"1-{capitale[indice]}")
        rep1.grid(row=2, sticky="w", padx=150)
        rep2 = tkinter.Label(app, text=f"2-{capitale[indice1]}")
        rep2.grid(row=2, sticky="n", padx=110)
        rep3 = tkinter.Label(app, text=f"3-{capitale[indice2]}")
        rep3.grid(row=2, sticky="se", padx=150)

    elif variation == 1:
        rep1 = tkinter.Label(app, text=f"1-{capitale[indice1]}")
        rep1.grid(row=2, sticky="w", padx=150)
        rep2 = tkinter.Label(app, text=f"2-{capitale[indice]}")
        rep2.grid(row=2, sticky="n", padx=110)
        rep3 = tkinter.Label(app, text=f"3-{capitale[indice2]}")
        rep3.grid(row=2, sticky="se", padx=150)

    elif variation == 2:
        rep1 = tkinter.Label(app, text=f"1-{capitale[indice1]}")
        rep1.grid(row=2, sticky="w", padx=150)
        rep2 = tkinter.Label(app, text=f"2-{capitale[indice2]}")
        rep2.grid(row=2, sticky="n", padx=110)
        rep3 = tkinter.Label(app, text=f"3-{capitale[indice]}")
        rep3.grid(row=2, sticky="se", padx=150)




def change_reponse_aleatoir():
    global indice1, indice2, rep1, rep2, rep3, variation


    indice1 = random.randrange(0, len(capitale))
    indice2 = random.randrange(0, len(capitale))
    variation = random.randrange(0, 3)

    #while indice1 == indice2 or indice1 == indice:
    if indice1 == indice2 or indice1 == indice :
        indice1 = random.randrange(0, len(capitale))
        indice2 = random.randrange(0, len(capitale))

    if variation == 0:
        rep1["text"] = f"1-{capitale[indice]}"
        rep2["text"] = f"2-{capitale[indice1]}"
        rep3["text"] = f"3-{capitale[indice2]}"

    elif variation == 1:
        rep1["text"] = f"1-{capitale[indice1]}"
        rep2["text"] = f"2-{capitale[indice]}"
        rep3["text"] = f"3-{capitale[indice2]}"

    elif variation == 2:
        rep1["text"] = f"1-{capitale[indice1]}"
        rep2["text"] = f"2-{capitale[indice2]}"
        rep3["text"] = f"3-{capitale[indice]}"















def desactive_bouton(name, name1):

    if name["state"] == "normal":
        name["state"] = "disabled"
        name1["state"] = "normal"



def active_entry():
    if entry_reponse["state"] == "disabled":
        entry_reponse["state"] = "normal"
        entry_reponse.delete(0, tkinter.END)



def score():
    global max_essai, essai, reponse_correcte, max_essai_label

    max_essai = 6
    essai = 0

    reponse_correcte = tkinter.Label(app, text=f"Score : {essai} pays / 3")
    reponse_correcte.grid(row=6, sticky="sw")

    max_essai_label = tkinter.Label(app, text=f"il te reste {max_essai}")
    max_essai_label.grid(row=6, sticky="se")

def score_change():
    global essai, max_essai
    reponse = entry_reponse.get()

    reponse = reponse.title()
    reponse = reponse.replace(' ', '')

    if reponse == capitale[indice]:
        essai += 1
        max_essai -= 1

        reponse_correcte["text"] = f"Score : {essai} pays / 3"


        max_essai_label["text"] = f"il te reste {max_essai}"


    else:
        max_essai -= 1
        reponse_correcte["text"] = f"Score : {essai} pays/3"
        if max_essai == 1 or max_essai == 0:
            max_essai_label["text"] = f"il te reste {max_essai} essai"
        else:
            max_essai_label["text"] = f"il te reste {max_essai} essais"
def reprise():

    valide_reponse["state"] = "normal"
    entry_reponse["state"] = "normal"
    entry_reponse.delete(0, tkinter.END)

    question_change1()
    resultat.destroy()
    score()
    #decompte()
    reprendre.destroy()



def game_over():
    global reprendre, essai, max_essai
    if essai == 3 or max_essai == 0:
        continuer["state"] = "disabled"
        entry_reponse["state"] = "disabled"
        valide_reponse["state"] = "disabled"
        reprendre = tkinter.Button(app, text="Reprendre", command=reprise)
        reprendre.grid()
    else:
        if max_essai == 6:
            reprendre.grid_forget()




"""

def decompte(count=15):
    m, s = divmod(count, 60)

    lab.config(text='{:02d}:{:02d}'.format(m, s))
    if count > 0:
        app.after(1000, decompte, count - 1)
    elif count == 0:
        resultat_fonc()
        score_change()
        game_over()

        if essai == 3 or max_essai == 0:
            continuer["state"] = "disabled"
        else:
            #if essai < 3 or max-essai > 0:
            desactive_bouton(valide_reponse, continuer)
            entry_reponse["state"] = "disabled"

"""



# si j'appuie ok le decompte s'arete
def stop_decompte():
    pass


















app = tkinter.Tk()
app.title("Ma capitale")

# taille minimale fenetre
app.minsize(640, 480)

# taille maximale fenetre
app.maxsize(640, 480)

# Menu

mainmenu = tkinter.Menu(app)

mon_menu = tkinter.Menu(mainmenu, tearoff=0)

mainmenu.add_cascade(label="Instructions", command= instruction)
mainmenu.add_cascade(label="A propos", command=  A_propo)
mainmenu.add_cascade(label="Quitter", command=app.quit)


name = tkinter.Label(app, text="*************************** Devine ma Capitale ***************************")
name.grid(padx=640/6, pady=10)





initialisation()

suite()

score()


lab = tkinter.Label(app, text='{:02d}:{:02d}'.format(3, 0))
lab.grid()
#decompte()

# Le Caire  regler les espaces
# gerer indice == indice2 ou indice == indice1 ou indice1 == indice2

# uppercase lowercase
# fichier











# Boucle principale
app.config(menu=mainmenu)
app.mainloop()












