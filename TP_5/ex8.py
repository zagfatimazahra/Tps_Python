def read_nonexistent_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            print("Contenu du fichier :")
            print(content)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_name}' est introuvable.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

# Exécution
if __name__ == "__main__":
    file_name = "inexistant.txt"
    read_nonexistent_file(file_name)
