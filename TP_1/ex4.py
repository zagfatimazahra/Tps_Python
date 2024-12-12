



def compte_occurences(liste):
    return{mots: liste.count(mots) for mots in set(liste)}

mots = ["amal","faty","faty","amal","faty","faty"]
resultat = compte_occurences(mots)
print(resultat)

