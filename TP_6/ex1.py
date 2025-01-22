def safe_division(a, b):
    try:
        result = a / b
        print("Résultat:", result)
    except ZeroDivisionError:
        print("Erreur : Division par zéro.")

safe_division(8,2)
safe_division(8,0)
