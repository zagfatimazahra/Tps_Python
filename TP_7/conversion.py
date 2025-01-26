def dollars_to_dirhams(dollars):
    if dollars < 0:
        raise ValueError("Le montant en dollars ne peut pas être négatif.")
    return dollars * 10

def meters_to_kilometers(meters):
    if meters < 0:
        raise ValueError("La distance en mètres ne peut pas être négative.")
    return meters / 1000