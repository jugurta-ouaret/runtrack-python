def calc(L):
    return L

L= list(range(1, 6))

print(calc(L))
print(calc(L)[1])

def remplacer(L):
    return L[3]
L[3]=L[2]+L[4]
print(calc(L))
print (calc(L)[-1])

    