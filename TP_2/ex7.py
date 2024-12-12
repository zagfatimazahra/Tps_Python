
class Livre:
    def __init__(self,titre,auteur,annee_publication):
         self.titre = titre
         self.auteur = auteur
         self.annee_publication = annee_publication

    def __str__(self):
        return f"{self.titre} écrit par {self.auteur} en {self.annee_publication}"


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre ajouté : {livre}")

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print("Livres dans la bibliothèque :")
            for livre in self.livres:
                print(f"- {livre}")
                
livre1 = Livre("Antigon","Sophocle", 1944)
livre2 = Livre("Atomic Habits","James Clear", 2018)
livre3 = Livre("White Garden","Sara", 2024)

biblio = Bibliotheque()
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.ajouter_livre(livre3)
biblio.afficher_livres()