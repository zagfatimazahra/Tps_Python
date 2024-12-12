class Animal:
    def faire_du_bruit(self):
        print("L'animal fait du bruit")

class Chein(Animal):
    def faire_du_bruit(self):
        print("Woof!")

class Chat(Animal):
    def faire_du_bruit(self):
        print("Miaou!")


animal = Animal()
animal.faire_du_bruit()
chein = Chein()
chein.faire_du_bruit()
chat = Chat()
chat.faire_du_bruit()