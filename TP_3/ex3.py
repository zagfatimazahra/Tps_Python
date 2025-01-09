def afficher_surface(formes):
    for forme in formes:
        print(f"Surface: {forme.calculer_surface()}")

formes = [Cercle(3), Rectangle(2, 5)]
afficher_surface(formes)