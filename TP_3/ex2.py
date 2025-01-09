class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom
            

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

personne = Personne(nom="Amani", prenom="Amal", age=25)
print(f"Nom: {personne.get_nom()}")
print(f"Prénom: {personne.get_prenom()}")
print(f"Age: {personne.get_age()}")

personne.set_nom("Zagrane")
personne.set_prenom("Fatima zahra")
print("***Update***")
print(f"Nom : {personne.get_nom()} | Prénom : {personne.get_prenom()}")








    
