def inverseur(L):
    return L

L = list(range(1, 6))

L[-5], L[-1] = L[-1], L[-5]

print(inverseur(L))
