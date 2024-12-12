


def analyse_texte(texte):
    mots = texte.split()
    nombre_mots = len(mots)
    nombre_caracteres = len(texte)
    return {"le nombre de mots est ": nombre_mots,
    "le nombre de caractéres est ": nombre_caracteres}


texte = "la maison est grand"
resultat = analyse_texte(texte)
print(resultat)