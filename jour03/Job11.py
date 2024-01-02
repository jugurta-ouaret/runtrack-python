def time_to_text(nombre):
    heures = nombre // 60
    minutes = nombre % 60
    return heures, minutes

resultat = time_to_text(128)
heures, minutes = resultat
print(f"{heures} heures et {minutes} minutes")
