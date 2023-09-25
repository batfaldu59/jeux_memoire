import os
import time
import random


def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def reponse_utilisateur(min, max):
    reponse_str = input(f"Votre choix de difficulté (entre {min} et {max}): ")
    try:
        reponse_int = int(reponse_str)
        if not min <= reponse_int <= max:
            print(f"ERREUR: vous devez entrer un nombre entre {min} et {max}!!!")
            return reponse_utilisateur(min, max)
        return reponse_int
    except ValueError:
        print("ERREUR: vous devez entrer une valeur numérique!!!")
        return reponse_utilisateur(min, max)


def choix_util_difficult(dictionnaire_niveau):
    index = 1
    print("----- Jeux de mémoire -----")
    print("Choisissez votre difficulté")
    for element in dictionnaire_niveau:
        print(f'{index}) {element["titre"]}')
        index += 1
    choix_utilisateur = reponse_utilisateur(1, len(dictionnaire_niveau))

    return dictionnaire_niveau[choix_utilisateur-1]


def definir_sequence(longeur):
    sequence = ""
    for i in range(longeur):
        chiffre_aleatoire = str(random.randint(0, 9))
        sequence += chiffre_aleatoire
    return sequence


NIVEAUX_DIFFICULTES = (
    {
        "titre": "Facile",
        "longeur_initiale": 3,
        "duree_affichage_seconde": 4,
        "increment_sequence": 1,
        "nombre_essais": 3
    },
    {
        "titre": "Normal",
        "longeur_initiale": 4,
        "duree_affichage_seconde": 3,
        "increment_sequence": 1,
        "nombre_essais": 2
    },
    {
        "titre": "Difficile",
        "longeur_initiale": 4,
        "duree_affichage_seconde": 2,
        "increment_sequence": 2,
        "nombre_essais": 1
    }
)


# Menu
choix_difficulte = choix_util_difficult(NIVEAUX_DIFFICULTES)

sequence = definir_sequence(choix_difficulte["longeur_initiale"])
clear_screen()
nombre_essais = choix_difficulte["nombre_essais"]
score = 0
print(f"Début du jeu - niveau {choix_difficulte['titre']}")

while True:
    print("Retenez la séquence")
    time.sleep(1)
    print(sequence)
    time.sleep(choix_difficulte["duree_affichage_seconde"])
    clear_screen()

    print(f"Nombre d'essais restants : {nombre_essais}")
    print(f"Votre score : {score}")
    seq_utilisateur = input("Votre réponse : ")
    if seq_utilisateur == sequence:
        score += 1
        sequence += definir_sequence(choix_difficulte["increment_sequence"])
        print("Bonne réponse !")
    else:
        nombre_essais -= 1
        if nombre_essais < 0:
            break
        print("Mauvaise réponse, réessayez")

    time.sleep(1)
    clear_screen()

print(f"Mauvaise réponse, la réponse était {sequence}")
print(f"Votre score est de {score}")