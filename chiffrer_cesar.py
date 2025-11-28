def chiffrer_cesar(texte, cle):
    resultat = ""
    for char in texte:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Décalage
            resultat += chr((ord(char) - base + cle) % 26 + base)
        else:
            resultat += char
    return resultat


def dechiffrer_cesar(texte, cle):
    return chiffrer_cesar(texte, -cle)


# Programme principal
print("=== Chiffrement César ===")
message = input("Entrez le message : ")
cle = int(input("Entrez la clé (ex: 3) : "))

message_chiffre = chiffrer_cesar(message, cle)
print("Message chiffré :", message_chiffre)

message_dechiffre = dechiffrer_cesar(message_chiffre, cle)
print("Message déchiffré :", message_dechiffre)