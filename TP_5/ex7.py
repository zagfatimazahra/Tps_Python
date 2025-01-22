import os
import shutil

# Fonction pour créer un fichier texte avec du contenu
def create_file(file_name, content):
    """Crée un fichier avec le nom donné et y ajoute du contenu."""
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Le fichier '{file_name}' a été créé avec succès.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la création du fichier : {e}")

# Fonction pour copier un fichier
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Le fichier '{source}' a été copié en '{destination}'.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{source}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la copie : {e}")

# Fonction pour déplacer un fichier
def move_file(source, destination_folder):
    try:
        os.makedirs(destination_folder, exist_ok=True)  # Crée le dossier s'il n'existe pas
        destination = os.path.join(destination_folder, os.path.basename(source))
        shutil.move(source, destination)
        print(f"Le fichier '{source}' a été déplacé dans le dossier '{destination_folder}'.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{source}' ou le dossier '{destination_folder}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue lors du déplacement : {e}")

# Exécution des opérations
if __name__ == "__main__":
    original_file = "journal.txt"
    copy_file_name = "journal_copie.txt"
    archive_folder = "archives"

    # Étape 1 : Créer le fichier "journal.txt"
    create_file(original_file, "Test\nTest")

    # Étape 2 : Copier le fichier vers "journal_copie.txt"
    copy_file(original_file, copy_file_name)

    # Étape 3 : Déplacer "journal_copie.txt" vers le dossier "archives"
    move_file(copy_file_name, archive_folder)
