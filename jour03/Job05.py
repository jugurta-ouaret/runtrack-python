def calcule(num1, opérateur, num2):
    if opérateur== "+":
     return num1+num2
    elif opérateur== "-":
     return num1-num2
    elif opérateur== "/":
     return num1/num2
    elif opérateur== "*":
     return num1*num2
    elif opérateur== "%":
     if num2 != 0:
       return num1%num2
     else:
       return "Opération Invalide"
    elif opérateur== "/":
     if num2 != 0:
       return num1/num2
     else:
       return "Opération Invalide"
     
resultat=calcule(10, "+", 3)
print(resultat)
     