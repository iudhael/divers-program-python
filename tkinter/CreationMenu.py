import tkinter


# add_checkbutton()
# add_radiobutton()
#add_separator




def hello():
    print("Coucou !")

def show_about():
    # fenetre supplementaire
    about_window = tkinter.Toplevel(app)
    about_window.title("A propos")
    lb = tkinter.Label(about_window, text="Bonjour !")
    lb.pack()



# cration et parametrage fenetre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Création de  Menu")





# widgets

mainmenu = tkinter.Menu(app)

first_menu  = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Hello", command=hello)
first_menu.add_separator()

#first_menu.add_checkbutton(label="lol")

first_menu.add_command(label="Option2")
first_menu.add_separator()
first_menu.add_command(label="Quitter", command=app.quit)

second_menu = tkinter.Menu(mainmenu, tearoff=0)

second_menu.add_command(label="Commande1")
second_menu.add_separator()
second_menu.add_command(label="A propos", command=show_about)



mainmenu.add_cascade(label="Premier", menu=first_menu)
mainmenu.add_cascade(label="Second", menu=second_menu)


# Boucle principale
app.config(menu=mainmenu)
app.mainloop()
