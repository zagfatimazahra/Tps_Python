
class Rectangle:
    def __init__(self,largeur,hauteur):
         self.largeur = largeur
         self.hauteur = hauteur
    @property
    def calculer_surface(self):
         return self.largeur * self.hauteur

    @property
    def calculer_perimetre(self):
         return (self.largeur + self.hauteur) * 2
        
rectangle1 = Rectangle(2, 3)
print(f"La surface de rectangle : {rectangle1.calculer_surface} m²")
print(f"La périmetre de rectangle : {rectangle1.calculer_perimetre} m")

