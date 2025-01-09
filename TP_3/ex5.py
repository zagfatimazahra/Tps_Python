class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employes = []

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def afficher_employes(self):
        for employe in self.employes:
            print(f"{employe.prenom} {employe.nom}")


employe1 = Employe("Alaoui","Ali",7000)
employe2 = Employe("Bari","Salma",8000)
manager = Manager("Chakori","Said",12000)

print("les employes :")
manager.ajouter_employe(employe1)
manager.ajouter_employe(employe2)
manager.afficher_employes()