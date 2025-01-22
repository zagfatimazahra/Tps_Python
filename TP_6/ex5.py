def process_input(user_input):
    try:
        number = int(user_input)
        result = number / 10
        print(f"Le résultat de la division est : {result}")
    except ValueError:
        print("Erreur : L'entrée doit être un entier valide.")
    except ZeroDivisionError:
        print("Erreur : Division par zéro impossible.")

process_input(10)
