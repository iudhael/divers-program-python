import random


uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}[];,.-!?/\\=+*&#"


upper, lower, nums, syms = True, True, True, False

all = ""

if upper:
    # si on choisit d'utiliser des lettres majuscule pour le mot de passe
    all += uppercase_letters

if lower:
    all += lowercase_letters

if nums:
    all += digits

if syms:
    all += symbols

length = 20 # taille du mot de passe a generer
amount = 10 # la quantité a generer

for x in range(amount):
    # joindre a la chaine de mot de passe 20 caractere de maniere aleatoire
    password = "".join(random.sample(all, length))
    print(password)


