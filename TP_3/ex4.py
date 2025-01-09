class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    def calculer_remise(self, remise):
        if self.__prix > 100:
            return self.__prix * (1 - remise / 100)
        return self.__prix

    def get_nom(self):
        return self.__nom

    def get_prix(self):
        return self.__prix


produit = Produit("Sac", 300)
print(f"Prix : {produit.get_prix()} DH")
print(f"Prix avec remise (-10%) : {produit.calculer_remise(10)} DH")