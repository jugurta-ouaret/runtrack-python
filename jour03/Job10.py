def pair_impair(num):
    if num%2== 0:
       print("Pair")
    else:
       print("impair")
    if num>0 and num%1==0:
       print(f"le nombre {num} est entier et positif")
    elif num>0 and num%1!=0:
       print(f"le nombre {num} est positif et n'est pas entier")
    elif num<0 and num%1==0:
       print(f"le nombre {num} est négatif et entier")
    elif num<0 and num%1!=0:
       print(f"le nombre {num} est négatif et n'est pas entier")

pair_impair(8.5)
pair_impair(-8.5)
pair_impair(7)
pair_impair(-6)