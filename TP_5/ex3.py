while True:
        reponse = input("Souhaitez-vous ajouter d'autres phrases ? (oui/non) : ").strip().lower()
        if reponse == "oui":
            with open("phrases.txt", "a") as file:
                phrase = input("Entrez une phrase à ajouter : ")
                file.write(phrase + "\n")
        elif reponse == "non":
            break
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")