import datetime


"""
comparer des date, recuperer des date dans des base de données ....
datetime.datetime(année, mois, jour, heure, minute, seconde)
        .date(année, mois, jour)
        .time (heure minute seconde)

"""

"""
d1 = datetime.datetime(2021, 7, 30, 14, 38)
print("jour 1 :",d1)
d2 = datetime.datetime(2021, 7, 29, 14, 38)
print("jour 2 :",d2)

print("Comparaison")
if d1 < d2:
    print("d1 est plus ancien que d2")
else:
    print("d1 est plus récent que d2")
"""

d1 = datetime.date(2021, 7, 27)
print("jour 1 :",d1)
d2 = datetime.date(2021, 7, 29)
print("jour 2 :",d2)

print("Comparaison")
if d1 < d2:
    print("d1 est plus ancien que d2")
else:
    print("d1 est plus récent que d2")



# recuperer l'anne , l'heure, mois ...
"""
.year, .month, .hour ...

"""
print(d1.year)

print("manipulatioon des heures")
t1 = datetime.time(14, 53, 40)
print(t1)

print("date du jour")
from datetime import  date

now  =date.today()
print(now)

print("date, heure, minutes, ...")
from datetime import  datetime


print(datetime.now())


""" probleme
print("\ncomparaison date du jour et ma date de naissance")
from datetime import  date

aujourdhuir = date.today()
born = datetime.date(2002, 11, 10)
print(f"{aujourdhuir.year - born.year} ans.")
"""
