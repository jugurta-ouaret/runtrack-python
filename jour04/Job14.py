def my_long_word(nombre, phrase):
    mots = phrase.split()
    mot_filtred=[mot for mot in mots if compteur(mot)== nombre]
    return mot_filtred

def compteur(mot):
    compte=0
    for _ in mot:
        compte += 1
    return compte

nombres= 5
phrases= "bonjours les amis voila !"
resultat= my_long_word(nombres, phrases)
print("output", resultat)
