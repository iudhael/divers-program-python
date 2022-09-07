import tkinter

"""
nom variable = nom_widgets(widget_parent, parametre)
widgets         :   Label(), Message(),

"""


app = tkinter.Tk()

# afficher du texte

label_welcom = tkinter.Label(app, text="Bienvenue à tous") # app est le widget parent

"""
# afficher les parametres d'un widget
print(label_welcom["text"])
# ou    print(label_welcom.cget("text"))

# modifier un parametre
label_welcom["text"] = "le nouveau message"
print(label_welcom["text"])
label_welcom.config(text = "Nouveau message")
print(label_welcom["text"])
"""


label_welcom.pack()

message_welcom = tkinter.Message(app, text="Bienvenue à tous")

message_welcom.pack()

# saisi
entry_name = tkinter.Entry(app, width=45)

"""
# saisi mot de passe cacher avec show
entry_name = tkinter.Entry(app, show="*")
"""
"""

entry_name.pack()

# widgets button
button_quit = tkinter.Button(app, text = "ok", width=25, height=2)


button_quit.pack()
"""
def hello():
    print("Hello sur le terminal !")

entry_name.pack()

# widgets button
button_quit = tkinter.Button(app, text = "ok", width=25, height=2, command=hello)


button_quit.pack()







app.mainloop()














