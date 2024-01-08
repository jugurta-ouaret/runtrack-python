def suprr(liste):
    sans_doublons = []
    for i in liste:
        if i not in sans_doublons:
            sans_doublons.append(i)
    return sans_doublons


liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
resultat = suprr(liste)

for i in resultat:
    print(i)



