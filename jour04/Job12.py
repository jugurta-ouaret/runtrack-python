L = [100, 32, 58, 76]
sorted_list = []

while L:
    min_num = L[0]
    for num in L:
        if num < min_num:
            min_num = num

    sorted_list.append(min_num)
    L.remove(min_num)

# Maintenant, la liste triée est dans sorted_list, tu peux l'afficher
for num in sorted_list:
    print(num)
