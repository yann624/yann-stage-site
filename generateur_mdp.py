import random

# 1. Demander la longueur du mot de passe
longueur = int(input("Longueur du mot de passe : "))

# 2. Définir les caractères possibles (ici : lettres minuscules seulement)
caracteres = "abcdefghijklmnopqrstuvwxyz"

mot_de_passe = ""

# 3. Boucle pour construire le mot de passe
for i in range(longueur):
    mot_de_passe += random.choice(caracteres)

# 4. Afficher le résultat
print("Mot de passe généré :", mot_de_passe)