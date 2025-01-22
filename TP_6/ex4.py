class NegativeAgeError(Exception):
    def __init__(self, age, message="L'âge ne peut pas être négatif."):
        self.age = age
        self.message = message
        super().__init__(f"{message} Age : {age}")

def set_age(age):
    if age < 0:
        raise NegativeAgeError(age)
    return f"Age : {age} ans."

try:
    print(set_age(22))
    print(set_age(-5))
except NegativeAgeError as e:
    print(f"Erreur : {e}")

