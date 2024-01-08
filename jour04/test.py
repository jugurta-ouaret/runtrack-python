nombre = 5.678

partie_decimale = nombre - int(nombre)  # Obtient la partie décimale du nombre

if partie_decimale > 0.5:
    nombre_arrondi = int(nombre) + 1
else:
    nombre_arrondi = int(nombre)

print(nombre_arrondi)