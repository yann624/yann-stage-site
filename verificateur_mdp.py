
# Vérificateur de sécurité de mot de passe
# Niveau : 3ème - pédagogie cybersécurité

def verifier_mot_de_passe(mdp):
    """Analyse un mot de passe et retourne un niveau de sécurité."""
    longueur = len(mdp)

    # Tests de base
    a_minuscule = any(c.islower() for c in mdp)
    a_majuscule = any(c.isupper() for c in mdp)
    a_chiffre   = any(c.isdigit() for c in mdp)
    speciaux = "!@#$%&*?+-_"
    a_special  = any(c in speciaux for c in mdp)

    score = 0

    # Longueur
    if longueur >= 8:
        score += 1
    if longueur >= 12:
        score += 1

    # Types de caractères
    if a_minuscule:
        score += 1
    if a_majuscule:
        score += 1
    if a_chiffre:
        score += 1
    if a_special:
        score += 1

    # Détermination du niveau en fonction du score
    if score <= 2:
        niveau = "FAIBLE"
    elif score <= 4:
        niveau = "MOYEN"
    else:
        niveau = "FORT"

    return niveau, {
        "longueur": longueur,
        "a_minuscule": a_minuscule,
        "a_majuscule": a_majuscule,
        "a_chiffre": a_chiffre,
        "a_special": a_special,
        "score": score
    }


def afficher_conseils(details):
    """Affiche des conseils pour améliorer le mot de passe."""
    print("\nConseils pour améliorer ton mot de passe :")

    if details["longueur"] < 8:
        print("- Utilise au moins 8 caractères.")
    elif details["longueur"] < 12:
        print("- Un mot de passe de 12 caractères ou plus est encore mieux.")

    if not details["a_minuscule"]:
        print("- Ajoute des lettres minuscules.")
    if not details["a_majuscule"]:
        print("- Ajoute des lettres MAJUSCULES.")
    if not details["a_chiffre"]:
        print("- Ajoute des chiffres (0–9).")
    if not details["a_special"]:
        print("- Ajoute des caractères spéciaux (ex : ! @ # $ % & * ? + - _).")

    if details["score"] >= 5:
        print("- Ton mot de passe est déjà très bon, garde-le secret et ne le partage jamais !")


# Programme principal
print("=== Vérificateur de sécurité de mot de passe ===")
mot_de_passe = input("Entre un mot de passe à tester : ")

niveau, infos = verifier_mot_de_passe(mot_de_passe)

print("\nRésultat de l'analyse :")
print(f"- Longueur : {infos['longueur']} caractères")
print(f"- Contient des minuscules : {infos['a_minuscule']}")
print(f"- Contient des MAJUSCULES : {infos['a_majuscule']}")
print(f"- Contient des chiffres    : {infos['a_chiffre']}")
print(f"- Contient des caractères spéciaux : {infos['a_special']}")
print(f"\n➡ Niveau de sécurité : {niveau}")

afficher_conseils(infos)
print("\nRappel :")
print("- Ne jamais utiliser ton vrai mot de passe dans un programme de test.")
print("- Ne pas utiliser le même mot de passe partout.")