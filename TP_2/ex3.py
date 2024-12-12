
class CompteBancaire:
    def __init__(self,titulaire,solde):
         self.titulaire = titulaire
         self.solde = solde
    
    def deposer(self, montant):
         self.solde += montant
         print(f"{montant} DH déposés. Nouveau solde: {self.solde} DH")

    def retirer(self, montant):
        if self.solde < montant:
            print("solde insuffisant")
        else:
            self.solde -= montant
            print(f"{montant} DH retirés. Nouveau solde: {self.solde} DH")

        
    def afficher_solde(self):
         print(f"le solde actuel : {self.solde} DH")

compteB1 = CompteBancaire("Hamza", 10000)
compteB1.afficher_solde()
compteB1.deposer(400)
compteB1.retirer(2000)

    

