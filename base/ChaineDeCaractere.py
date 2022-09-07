# classe str : string (chaine de caractere)

# pour voir la documentation faire : help(str)

"""
# str.upper() : met la chaine en majuscule
# str.lower() : met la chaine en miniscule
# str.capitalize() : met le debut du mot premier mot de la chaine en majuscule
# str.title() : met le debut de chaque mot en majuscule
# str.center(<largeur>, <caractere_remplissage>) : modifier l'affichage
# str.find(<chaine>, <debut>, <fin>) : cherche une chaine vers un debut ou une fin
# str.index(<chaine>, <debut>, <fin>) : cherche une chaine vers un debut ou une fin
# str.strip() : enleve tous les espaces
# str.replace(<ancienne>, <nouvelle>, <occurences>)

# coupure de chaine pour la transformer en liste # str.split(<separateur>)


une methode de chaine travaille sur une copie et pas sur la chaine elle meme

str.isalpha(), str.isdigit(), str.isnumeric(), str.isalphanum()

str.islower() : verifier si une chaine est ecrit en miniscule
str.isupper() : verifier si une chaine est ecrit en majuscule

str.isidentifier(), str.iskeyword()
"""
"""
ma_chaine = "Bonjour tout le monde"

# str.upper() : met la chaine en majuscule
ma_chaine = ma_chaine.upper()
print(ma_chaine)

# str.lower() : met la chaine en miniscule
ma_chaine = ma_chaine.lower()
print(ma_chaine)

# str.capitalize() : met le debut du mot premier mot de la chaine en majuscule
ma_chaine = ma_chaine.capitalize()
print(ma_chaine)

# str.title() : met le debut de chaque mot en majuscule
ma_chaine = ma_chaine.title()
print(ma_chaine)

ch1 = "MonSuperProgramme"
print(ch1)
# str.center(<largeur>, <caractere_remplissage>) : modifier l'affichage
ch1 = ch1.center(40, "-")
print(ch1)
"""
ch1 = "MonSuperProgramme"
# str.find(<chaine>, <debut>, <fin>) : cherche une chaine vers un debut ou une fin
print(ch1[2])  # affiche le caractere d'indice 2 qui est n
print(ch1.find("Super"))  # indique que la  chaine debute a  d'indice 3
"""
# str.index(<chaine>, <debut>, <fin>) : cherche une chaine vers un debut ou une fin
ch1 = "MonSuperProgramme"
try:
    print(ch1.index("super"))  # indique que la  chaine debute a  d'indice 3
except ValueError:
    print("Je n'ai pas trouvé")

# str.strip() : enleve tous les espaces
ch2 = "          MonSuperProgramme"
print(ch2.strip())
ch2 = "[     MonSuperProgramme     ]"
print(ch2.strip())

# str.replace(<ancienne>, <nouvelle>, <occurences>)
ch3 = "booooooooooooooombooom"
print(ch3)
ch3 = ch3.replace("o", "a")
print(ch3)
ch3 = ch3.replace("a", "o", 2)  # le 3ieme parametre n'est pas obligatoire et change les 2 premiers a
print(ch3)

# coupure de chaine pour la transformer en liste
# str.split(<separateur>)
phrase = "Magicien|10|5"

print(phrase.split("|"))  # | est le séparateur

# str.islower() : verifier si une chaine est ecrit en miniscule
ch = "Bonjour"
print(ch)
if ch.islower():
    print("Minuscule")
else:
    print(ch + "  " + "Contient une ou des majuscule(s)")

# isidentifier()
if ch.isidentifier():
    print("Réservé")
else:
    print("Libre")

ch4 = "le langage python"
if "langage" in ch4:
    print("le mot 'langage' est trouvé dans " + "<" + ch4 + ">")
else:
    print("Non trouvé")
"""