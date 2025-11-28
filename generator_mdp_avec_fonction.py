import random

def generer_mot_de_passe(longueur):
    minuscules = "abcdefghijklmnopqrstuvwxyz"
    majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chiffres = "0123456789"
    speciaux = "!@#$%&*?+-_"

    tous = minuscules + majuscules + chiffres + speciaux
    mot = ""

    # 1 minuscule + 1 majuscule + 1 chiffre + 1 spécial
    mot += random.choice(minuscules)
    mot += random.choice(majuscules)
    mot += random.choice(chiffres)
    mot += random.choice(speciaux)

    for i in range(longueur - 4):
        mot += random.choice(tous)

    mot_liste = list(mot)
    random.shuffle(mot_liste)
    return "".join(mot_liste)


print("=== Générateur de mots de passe ===")

longueur = int(input("Choisis la longueur du mot de passe : "))

if longueur < 8:
    print("❌ Erreur : la longueur doit être au minimum de 8 caractères.")
else:
    mdp = generer_mot_de_passe(longueur)
    print("Ton mot de passe généré est :", mdp)