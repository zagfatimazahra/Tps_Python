class Chien:
    def __init__(self,nom,race,age):
         self.nom = nom
         self.race = race
         self.age = age


    def aboyer(self):
        print("Woof!")

C1=Chien('pitbul','terrier',3)
C1.aboyer()
