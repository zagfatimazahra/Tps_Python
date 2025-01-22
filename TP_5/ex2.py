with open("phrases.txt", "w") as file:
        for i in range(3):
            phrase = input(f"Entrez la phrase {i + 1} : ")
            file.write(phrase + "\n")
    
