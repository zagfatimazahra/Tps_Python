class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []

    def se_presenter(self):
        print(f"je m'appelle {self.prenom} {self.nom}, j'ai {self.age} ans.")

    def ajouter_ami(self, ami):
        if ami not in self.amis:
            self.amis.append(ami)
            print(f"{ami.prenom} {ami.nom} est devenez votre ami(e).")
        else:
            print(f"{ami.prenom} {ami.nom} est déjà dans la liste d'amis.")

    def afficher_amis(self):
        if not self.amis:
            print("Aucun ami(e) pour l'instant.")
        else:
            print("Mes amis :")
            for ami in self.amis:
                print(f"- {ami.prenom} {ami.nom}")

personne1 = Personne("Amal","sami",25)
personne2 = Personne("Kawtar","sami",23)
personne3 = Personne("Rimal","Rawi",24)

personne1.se_presenter()
personne1.ajouter_ami(personne2)
personne1.ajouter_ami(personne3)
personne1.se_presenter()
personne1.ajouter_ami(personne2)
personne1.afficher_amis()