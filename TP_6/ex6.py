def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erreur : Division par zéro n'est pas autorisée.")
    else:
        print("La division a été effectuée avec succès.")
        return result
    finally:
        print("La fonction safe_division est terminée.")

print(safe_division(20, 2))