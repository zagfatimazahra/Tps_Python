with open("C:\\Users\\Administrator\\Desktop\\Study\\CODES\\TPs_Python\\TP 5\\phrases.txt", "w") as file:
        for i in range(3):
            phrase = input(f"Entrez la phrase {i + 1} : ")
            file.write(phrase + "\n")
    
