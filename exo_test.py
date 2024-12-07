import csv

# Lecture d'un fichier CSV
def importer_table(fichier):
    with open(fichier, mode='r', newline='', encoding='utf-8') as f:
        lecteur = csv.DictReader(f, delimiter=';')
        return [ligne for ligne in lecteur]

table = importer_table("2020_fictif_prenoms-enfants-nes-nantes.csv")
print(table)
def occurrence_prenom_fille(table1, prenom):
    nb_fois_prenom=0
    for ligne in table1 : 
        if ligne['Prénom'].upper() == prenom.upper() and ligne['Sexe'] == 'FILLE' and float(ligne['Occurence']) > 5 :
            nb_fois_prenom = nb_fois_prenom + float(ligne['Occurence'])
            print(nb_fois_prenom)
    return nb_fois_prenom

print("Résultat :")
print(occurrence_prenom_fille(table, 'AGATHE'))