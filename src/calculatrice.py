import sys


choix = ""
while choix != 'non':
    # On demande deux à l'utilisateur
    num1 = input("Veuillez entrer un premier nombre : ")
    num2 = input("Veuillez entrer un deuxième nombre : ")

    # On affiche une phrase si les nombres entrés ne sont pas valides.
    if (not num1.isdigit() or not num2.isdigit()):
        print("Veuillez entrer deux nombres valides")
    else:
        # On affiche le resultat de l'addition
        resultat = f"Le résultat de l'addition du nombre {num1} avec le nombre {num2} est égal à {int(num1) + int(num2)}"
        print(resultat)
    choix = input("Avez-vous d'autres nombres à additionner ? oui/non ")
    if choix == 'oui':
        continue
print("==Fin de notre programme==")
sys.exit()