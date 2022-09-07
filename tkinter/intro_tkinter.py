import tkinter

# tout ce qui est fenetre, champ de saisie,... est un widget

mainapp = tkinter.Tk()
mainapp.title("Mon premier programme fenetre")
"""
# taille minimale fenetre
mainapp.minsize(640, 480)

# taille maximale fenetre
mainapp.maxsize(1280, 720)

# interdire le dimensionnement d'un cote ou des deux 
mainapp.resizable(width= False, height= True)
mainapp.positionfrom("user")
mainapp.sizefrom("user")

"""
"""
# dimension fenetrre geometry("XxY+0+0")
mainapp.geometry("800x600+50+100")
"""

# centrer la fenetre
"""
position_x = (largeur_ecran // 2) - (largeur_fenetre // 2)
position_y = (hauteur_ecran // 2) - (hauteur_fenetre // 2)
"""
screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())
window_x = 800
window_y = 600

posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
mainapp.geometry(geo)

# boucle infinie pour eviter que la fenetre se referme directement
mainapp.mainloop()







