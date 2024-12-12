
class Personne:
    def __init__(self,nom,prenom,age):
         self.nom = nom
         self.prenom = prenom
         self.age = age

    def se_presenter(self):
        print(f"Je m'appelle {self.prenom} {self.nom}, j'ai {self.age} ans.")
    
class Etudiant(Personne):
    def __init__(self,nom,prenom,age,matricule):
        super().__init__(nom,prenom,age)
        self.matricule = matricule

    def etudier(self):
        print(f"{self.prenom} {self.nom} est un étudaint(e) et son matricule est : {self.matricule}.")


personne1 = Personne("Zagrane","Fatima zahra",23)
personne1.se_presenter()
etudaint1 = Etudiant("Alami","Amir",24,"D13809060")
etudaint1.se_presenter()
etudaint1.etudier()
