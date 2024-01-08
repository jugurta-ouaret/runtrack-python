
liste_nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


i = 0
for nombre in liste_nombres:
    partie_decimale = nombre - int(nombre)
    if partie_decimale >= 0.5:  
        liste_nombres[i] = int(nombre) + 1
    else:
        liste_nombres[i] = int(nombre)
    i += 1


print(liste_nombres)
