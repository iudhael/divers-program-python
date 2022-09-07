import tkinter

app = tkinter.Tk()
app.geometry("500x500")


# checkbox case a cocher ou pas
# check_widget = tkinter.Checkbutton(app, text= "Publier", offvalue=2, onvalue=5)
check_widget = tkinter.Checkbutton(app, text= "Publier")

radio_widget = tkinter.Radiobutton(app, text="Homme", value=1)
radio_widget2 = tkinter.Radiobutton(app, text="Femme", value=0)

# pour changer la fourchette d'intervalle on fait from_= valeur depart to=valeur fin
scale_w = tkinter.Scale(app, from_=10, to=100, tickinterval=25)
spin_w = tkinter.Spinbox(app, from_=1, to=10)

# liste d'element liste box
lb = tkinter.Listbox(app)


# ajout des element de la liste
lb.insert(1, "windows")
lb.insert(2, "GNU/Linux")
lb.insert(3, "MacOS")

# fenetre modale : message d'erreur d'avertissement...
from tkinter import messagebox
""""
showerror
showinfo
showwarning
askquestion
askokcancel
askyesno
askretrycancel


"""
def show_modal_window():
    messagebox.showerror("ERREUR", "Un probleme est survenu !")

btn = tkinter.Button(app, text="Déclencher une erreur", command=show_modal_window)


def show_modal_window1():
    messagebox.askquestion("Sondage", "Etes vous humain ?")

btn1 = tkinter.Button(app, text="Sondage", command=show_modal_window1)


def show_modal_window2():
    messagebox.askokcancel("Avertissement", "Continuer ?")

btn2 = tkinter.Button(app, text="test", command=show_modal_window2)



check_widget.pack()

radio_widget.pack()
radio_widget2.pack()

scale_w.pack()
spin_w.pack()

lb.pack()

btn.pack()
btn1.pack()
btn2.pack()

app.mainloop()















