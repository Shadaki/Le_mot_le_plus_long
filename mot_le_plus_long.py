#!/usr/bin/python3

import random

fichier = open("mots_francais.txt", "r")
mots = fichier.readlines()
tirees = []
for i in range(9):
    n = random.randrange(1, 100)
    if n < 44:
        tirees.append(random.choice(list("AEIOUY")))
    else:
        tirees.append(random.choice(list("BCDFGHJKLMNPQRSTVWXZ")))
tirees.sort()
print("Tirage :", " ".join(tirees))

lenMax, motMax = 0, ""
for mot in mots:
    ok = True
    tmpTirees = tirees[:]
    lettresMot = list(mot)[:-1]
    for l in lettresMot:
        if l in tmpTirees:
            tmpTirees.remove(l)
        else:
            ok = False
    if ok and len(mot) > lenMax:
        lenMax = len(mot)
        motMax = mot
    if motMax == 9:
        break

print("\nLe mot trouvé comporte", lenMax - 1, "lettres.")
print("Mot trouvé :", motMax)
