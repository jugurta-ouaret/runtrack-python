def ma_fonction(type, saison):
    if type == "fruits" and saison=="hiver":
        return "orange, mandarine et kiwi"
    elif type == "fruits" and saison=="ete":
        return "Poire, fraise, cassis"
    elif type == "legume" and saison=="hiver":
        return "carotte, topinambour, endive"
    elif type == "legume" and saison=="ete":
        return "artichaut, aubergine,navet"

resultat=ma_fonction("fruits", "hiver")
print(resultat)
    
    