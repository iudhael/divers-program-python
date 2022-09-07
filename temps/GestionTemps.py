import time

"""
time.sleep(seconde)
time.time()
time.localtime()
time.mktime(time.localtime)

"""

# date de depart du temps en informatique
    # 1er Janvier 1970 à 00h00  (TIMESTAMP)
""" a partie de cette date on a decompter le nomblre de seconde qui s'écoulait

# recuperer le temps ecouler
print(time.time())



# connaitre le temps ecouler
begin = time.time()
print("Debut")

time.sleep(5)

end = time.time()
print("Fin")

print(f"Temps exécuté : {end - begin}s")

"""

"""
print(time.localtime()) # donne des informations

                localtime : print(time.localtime())
(TIMESTAMP)     ------------>   structure de temps
                <------------
                mktime()    # chemin inverse
                tps = time.localtime()
                print(tps)

                tps = time.mktime(tps)  
                print(tps)
                
                
"""

# avoir une chaine pour manipuler du temps avec 'strftime'
""" forma du strftime
%d : jour (01 a 31)
%m : mois (01 à 12)
%Y : année (exemple : 2021) ou %y ( 00 à 99 )
%H : heures (00 à 24)
%I : minutes (00 à 59)
%S : secondes (00 à 59)
%p : AM/PM (heur anglaise)


%A : jour semaine / %a (jour abrégé)
%B : mois / %b (mois abrégé)

%Z : fuseau horaire (timezone

"""
my_time = time.strftime("%d/%m/%Y")
print(my_time)

my_time = time.strftime("%Z")
print(my_time)

my_time = time.strftime("Il est %Hh %Imin %Ssec")
print(my_time)

