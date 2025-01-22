def get_positive_integer():
    while True:
        try:
            user_input = input("entrer un entier positif : ")
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("L'entier doit être strictement positif. Veuillez réessayer.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

if __name__ == "__main__":
    result = get_positive_integer()
    print(f"Vous avez entré : {result}")
