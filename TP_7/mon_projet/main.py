from src.math_operations import add, subtract, multiply, divide
from src.string_operations import concatenate, to_uppercase

def main():
    # Opérations mathématiques
    print("Addition: 2 + 3 =", add(2, 3))
    print("Soustraction: 10 - 5 =", subtract(10, 5))
    print("Multiplication: 4 * 3 =", multiply(4, 3))
    print("Division: 10 / 2 =", divide(10, 2))

    # Opérations sur les chaînes de caractères
    print("Concaténation: 'ZAGRANE' + ' FATIMA ZAHRA' =", concatenate("Zagrane", " FATIMA ZAHRA"))
    print("Majuscules: 'zagrane' =", to_uppercase("zagrane"))

if __name__ == "__main__":
    main()