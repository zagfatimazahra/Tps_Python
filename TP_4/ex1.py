class VehiculeTransport:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"Véhicule : {self.marque} {self.modele}, Année : {self.annee}")

class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        print(f"Moteur : {self.puissance} chevaux, Type : {self.type_moteur}")

class VoitureTransport(VehiculeTransport, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        VehiculeTransport.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print(f"Nombre de places : {self.nombre_de_places}")

class Moto(VehiculeTransport, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        VehiculeTransport.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print(f"Type de moto : {self.type_moto}")

voiture = VoitureTransport(marque="DACIA", modele="DOSTER", annee=2025, puissance=500, type_moteur="Essence", nombre_de_places=5)
moto = Moto(marque="MOTORX", modele="MODE", annee=2016, puissance=440, type_moteur="Essence", type_moto="Sport")

print("Informations sur la voiture :")
voiture.afficher_info()

print("\nInformations sur la moto :")
moto.afficher_info()

print(VoitureTransport.mro())

