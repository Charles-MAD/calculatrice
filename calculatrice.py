import sys

while True:
    # On demande deux à l'utilisateur
    a = input("Veuillez entrer un premier nombre : ")
    b = input("Veuillez entrer un deuxième nombre : ")

    # On affiche une phrase si les nombres entrés ne sont pas valides.
    if (not a.isdigit() or not b.isdigit()):
        print("Veuillez entrer deux nombres valides")
    else:
        # On affiche le resultat de l'addition
        resultat = f"Le résultat de l'addition du nombre {a} avec le nombre {b} est égal à {int(a) + int(b)}"
        print(resultat)
    choix = input("Avez-vous d'autres nombres à additionner ? oui/non ")
    if choix == 'oui':
        continue
    else:
        print("==Fin de notre programme==")
        sys.exit()