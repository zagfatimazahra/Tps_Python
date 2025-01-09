from abc import ABC, abstractmethod
class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass

class Voiture(Vehicule):
    def deplacer(self):
        print("La voiture roule sur la route.")

class Bicyclette(Vehicule):
    def deplacer(self):
        print("La bicyclette est pédalée sur le chemin.")


voiture = Voiture()
bicyclette = Bicyclette()

voiture.deplacer()
bicyclette.deplacer()