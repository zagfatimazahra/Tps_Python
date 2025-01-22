import os

# Fonction pour renommer un fichier
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Le fichier '{old_name}' a été renommé en '{new_name}'.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{old_name}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Fonction pour supprimer un fichier
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"Le fichier '{file_name}' a été supprimé.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_name}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exécution des opérations
if __name__ == "__main__":
    old_file = "phrases.txt"
    new_file = "anciennes_phrases.txt"
    
    # Renommer le fichier
    rename_file(old_file, new_file)
    
    # Supprimer le fichier
    delete_file(new_file)
