class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total(self):
        total = sum(commande.produit.prix * commande.quantite for commande in self.commandes)
        return total
        
p1 = Produit(nom="Sac LV", prix=13000)
p2 = Produit(nom="Sac Channel", prix=12000)
p3 = Produit(nom="Sun Glass", prix=3000)
commande1 = Commande(produit=p1, quantite=1)
commande2 = Commande(produit=p2, quantite=1)
commande3 = Commande(produit=p3, quantite=2)

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)
panier.ajouter_commande(commande3)
print(f"Total : {panier.calculer_total()} DH")