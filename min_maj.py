import random

longueur = int(input("Longueur du mot de passe : "))

minuscules = "abcdefghijklmnopqrstuvwxyz"
majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
speciaux = "!@#$%&*?+-_"

# On rassemble tous les types de caractères
caracteres = minuscules + majuscules + chiffres + speciaux

mot_de_passe = ""

for i in range(longueur):
    mot_de_passe += random.choice(caracteres)

print("Mot de passe sécurisé :", mot_de_passe)