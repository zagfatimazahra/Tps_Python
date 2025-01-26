import os
from datetime import datetime
from math import sqrt

def main():
    # 1. Afficher le répertoire courant
    current_directory = os.getcwd()
    print(f"Répertoire courant : {current_directory}")

    # 2. Afficher la date et l'heure actuelles
    current_datetime = datetime.now()
    print(f"Date et heure actuelles : {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

    # 3. Calculer et afficher la racine carrée d'un nombre donné par l'utilisateur
    try:
        number = float(input("Entrez un nombre pour calculer sa racine carrée : "))
        if number < 0:
            print("Erreur : la racine carrée d'un nombre négatif n'est pas définie dans les réels.")
        else:
            result = sqrt(number)
            print(f"La racine carrée de {number} est {result}.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()
