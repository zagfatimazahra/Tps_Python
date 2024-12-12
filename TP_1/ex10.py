

def fusionner_dicts(dict1, dict2):
    fusiond = dict1.copy()
    for cle, valeur in dict2.items():
        fusiond[cle] = fusiond.get(cle, 0) + valeur
    return fusiond

dict1 = {"faty": 12, "amal": 4}
dict2 = {"samir": 9, "amal": 6}
print(fusionner_dicts(dict1, dict2))