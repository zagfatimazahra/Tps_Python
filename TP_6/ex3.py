def read_file(filename):
    try:
        with open(filename,"r") as fichier:
            contenu = fichier.read()
            print(contenu)

    except FileNotFoundError:
            print("Erreur : ce fichier nexist pas")

    finally :
        print("Fin de la gestion de fichier")

read_file("C:\\Users\\Administrator\\Desktop\\Study\\CODES\\PYTHON_TPS\\TP 6\\exemple.txt")
read_file("fichier.txt")

