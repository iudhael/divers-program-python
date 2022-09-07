import tkinter

# cration et parametrage fenetre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Positionnement Widgets")




# widgets
"""
# widget permettant de creer des cadres pouvant contenir d'autres widgets 
mainframe = tkinter.Frame(app, width=300, height=200, borderwidth=1)
mainframe.pack()
# mettre le bouton dans le cadre  en mettant comme paramettre parent le cadre

btn = tkinter.Button(mainframe, text="BIENVENUE")
btn.pack()

# cadre nommer
mainframe = tkinter.LabelFrame(app, text="Titre", width=300, height=200, borderwidth=1)

mainframe.pack()

btn = tkinter.Button(app, text="BIENVENUE")
btn.pack()
"""

# positionnement trois cas
    # methode pack()
"""
pack peut prendre comme parametre :

    side="top" ou "bottom" ou "right" ou "left"
    expand=0 ou 1 ( extension occupe toute l'espace )
    fill = "y" ou "x" ou "both" ou "none"
    padx= un nombre ( marge exterieur )
    pady= un nombre ( marge exterieur )
    ipadx, ipady marges interieur


"""

    # methode grid()
"""
grid prend comme parametre

    row = entier
    column = entier
    columnspan = entier ( nombre de colonne )
    rowspan = entier
    padx, pady, ipadx, ipady
    sticky ="n" ou "s" ou "e" ou "w" ou "ne" ...
            prends comme valeur n --> nord
                                s --> sud
                                e --> est
                                w --> ouest
                                ne --> nord est
                                
                                
    label = tkinter.Label(app, text="un label")
ent = tkinter.Entry(app)
btn = tkinter.Button(app, text="BIENVENUE")




label.grid(sticky="e")
ent.grid()
btn.grid()


"""
# mathode place()
"""
prends comme valeurs :
    x = entier, y = entier


"""

btn = tkinter.Button(app, text="BIENVENUE")
btn.place(x=100, y=10)


# Boucle principale
app.mainloop()
