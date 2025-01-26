def add(a, b):
    """ L'addition """
    return a + b

def subtract(a, b):
    """ Soustraction """
    return a - b

def multiply(a, b):
    """ Multiplication """
    return a * b

def divide(a, b):
    """ Division """
    if b == 0:
        raise ValueError("Erreur : La division par zéro n'est pas autorisée.")
    return a / b
