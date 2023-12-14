def est_nombre_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, nombre):
        if nombre % i == 0:
            return False
    return True

# Afficher les nombres premiers entre 0 et 1000
for nombre in range(1001):
    if est_nombre_premier(nombre):
        print(nombre)

