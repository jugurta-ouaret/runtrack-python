L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

valeurs_paires = [valeur for valeur in L if valeur % 2 == 0]


somme_paires = sum(valeurs_paires)

print("La somme des valeurs paires dans la liste est :", somme_paires)
