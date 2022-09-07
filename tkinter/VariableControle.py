import tkinter

"""
    variables nommées
StringVar()     : chaine de caractere [str]
IntVar()        : nombre entier [int]
DoubleVar()     : nombre flottant [float]
BooleanVar()    : Booléen [bool]

"""
# creer un observateur
def update_observeur(*args):
    # *args : pour accepter plusieurs variable
    var_label.set(var_entry.get())



# creation et parametrage de la fenetre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variable Controle")


# widgets...
var_entry = tkinter.StringVar()
# on surveille la variable var_entry connecter avec 'trace' a la fonction update_observeur
var_entry.trace("w", update_observeur)

entry = tkinter.Entry(app, textvariable = var_entry)


var_label = tkinter.StringVar()
label = tkinter.Label(app, textvariable=var_label)
var_label.set("Le label...")
print(("Label :", var_label.get()))

"""
******************************************************
"""
# creer un  autre observateur
def update_observeur1(*args):
    # *args : pour accepter plusieurs variable
    if var_gender.get():
        #print(f"Sexe :{var_gender.get()}")
        var_label_gender.set("C'est un Homme")

    else:
        var_label_gender.set("C'est une Femme")

var_gender = tkinter.IntVar()
var_gender.trace("w", update_observeur1)

# pour RadioButton et CheckButton utiliser 'variable' au lieu de 'textvariable'
radio1 = tkinter.Radiobutton(app, text="Homme", value=1, variable=var_gender)
radio2 = tkinter.Radiobutton(app, text="Fomme", value=0, variable=var_gender)

var_label_gender = tkinter.StringVar()
label_gender = tkinter.Label(app, textvariable=var_label_gender)

""" supprimer l'observateur
trace_vedelete("u", nom de l'observateur)

"""



entry.pack()
label.pack()
radio1.pack()
radio2.pack()
label_gender.pack()


# boucle principale
app.mainloop()