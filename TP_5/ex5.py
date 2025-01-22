import json

# Fonction pour créer et enregistrer un dictionnaire dans un fichier JSON
def write_students_to_json(file_name):
    students = [
        {"nom": "Alice", "âge": 23, "note": 19.0},
        {"nom": "Alame", "âge": 22, "note": 15.0},
        {"nom": "Othmani", "âge": 21, "note": 20.0}
    ]

    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(students, file, ensure_ascii=False, indent=4)
        print(f"Les informations des étudiants ont été enregistrées dans '{file_name}'.")
    except Exception as e:
        print(f"Une erreur est survenue lors de l'écriture dans le fichier JSON : {e}")

# Fonction pour lire un fichier JSON et afficher les informations
def read_students_from_json(file_name):
    """Lit un fichier JSON et affiche les informations des étudiants."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            students = json.load(file)
            print("Informations des étudiants :")
            for student in students:
                print(f"Nom : {student['nom']}, Âge : {student['âge']}, Note : {student['note']}")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_name}' est introuvable.")
    except json.JSONDecodeError:
        print(f"Erreur : Le fichier '{file_name}' n'est pas un JSON valide.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exécution des fonctions
if __name__ == "__main__":
    json_file = "etudiants.json"
    
    # Enregistrer les informations dans un fichier JSON
    write_students_to_json(json_file)
    
    # Lire et afficher les informations du fichier JSON
    read_students_from_json(json_file)
