

class Voiture:
    def __init__(self,marque,modele,annee):
         self.marque=marque
         self.modele=modele
         self.annee=annee

    def afficher_info(self):
        print(self.marque , self.modele ,self.annee)

voiture1 = Voiture("Odi", "Model 1", 2023)
voiture2 = Voiture("Dacia", "Model 1", 2018)

voiture1.afficher_info()
voiture2.afficher_info()

        
        
