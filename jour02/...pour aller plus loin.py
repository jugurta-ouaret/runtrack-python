def type_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Équilatéral."
        elif a == b or a == c or b == c:
            return "Isocèle." if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else "Isocèle mais pas rectangle."
        else:
            return "Rectangle." if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else "Quelconque."
    else:
        return "Impossible de former un triangle."

a, b, c = map(float, input("Entrez les longueurs a, b, c séparées par des espaces : ").split())
print(type_triangle(a, b, c))
