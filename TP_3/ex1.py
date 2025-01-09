from abc import ABC, abstractmethod

class Forme(ABC): # Class Abstraite
    @abstractmethod
    def calculer_surface(self): # Méthode Abstraite
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    
    def calculer_surface(self):
        return 3.14159 * self.rayon ** 2

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def calculer_surface(self):
        return self.longueur * self.largeur

cercle = Cercle(4)
rectangle = Rectangle(5, 8)

print(f"Surface du cercle : {cercle.calculer_surface()}")
print(f"Surface du rectangle : {rectangle.calculer_surface()}")
