def moyenne(note1, note2, note3):
    moyenne_etudiant= (note1+note2+note3)/3
    return moyenne_etudiant
note1= float(input("Entrez votre note1: "))
note2= float(input("Entrez votre note2: "))
note3= float(input("Entrez votre note3: "))

moyenne_etudiant=moyenne(note1, note2, note3)
print(moyenne_etudiant)

i=moyenne_etudiant

if 15<= moyenne_etudiant <=20:
    print("Très Bon élève")
if 11<= moyenne_etudiant <=14:
    print("Bon élève")
if 8<= moyenne_etudiant <=10:
    print("Élève moyen")
if 0<= moyenne_etudiant <=7:
    print("Élève devant faire des efforts")