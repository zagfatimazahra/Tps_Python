def file_statistics(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Calcul des statistiques
        total_lines = len(lines)
        total_words = sum(len(line.split()) for line in lines)
        total_characters = sum(len(line) for line in lines)

        # Affichage des résultats
        print(f"Statistiques du fichier '{file_name}':")
        print(f"- Nombre total de lignes : {total_lines}")
        print(f"- Nombre total de mots : {total_words}")
        print(f"- Nombre total de caractères : {total_characters}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_name}' est introuvable.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

# Exécution du script
if __name__ == "__main__":
    file_name = "exemple.txt" 
    file_statistics(file_name)
