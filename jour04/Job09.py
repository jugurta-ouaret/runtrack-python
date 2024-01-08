plus_petit_nombre = float('inf') 
plus_grand_nombre = float('-inf')  

# Parcourir la liste
for i in [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]:
    if i < plus_petit_nombre:
        plus_petit_nombre = i
    if i > plus_grand_nombre:
        plus_grand_nombre = i

print("Le plus petit nombre dans la liste est :", plus_petit_nombre)
print("Le plus grand nombre dans la liste est :", plus_grand_nombre)
