import csv
import os

# Nom du fichier CSV
CSV_FILE = "contacts.csv"

# Initialisation du fichier CSV avec en-têtes s'il n'existe pas
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nom", "Téléphone", "Email"])
            print(f"Le fichier '{CSV_FILE}' a été créé.")

# Ajouter un contact
def add_contact():
    nom = input("Entrez le nom : ")
    telephone = input("Entrez le téléphone : ")
    email = input("Entrez l'email : ")

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([nom, telephone, email])
        print("Contact ajouté avec succès !")

# Afficher tous les contacts
def display_contacts():
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            contacts = list(reader)

            if len(contacts) > 1:
                print("\nListe des contacts :")
                for i, contact in enumerate(contacts[1:], start=1):  # Ignorer l'en-tête
                    print(f"{i}. Nom : {contact[0]}, Téléphone : {contact[1]}, Email : {contact[2]}")
            else:
                print("\nAucun contact trouvé.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{CSV_FILE}' est introuvable.")

# Rechercher un contact
def search_contact():
    nom_recherche = input("Entrez le nom à rechercher : ")
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            found = False

            for contact in reader:
                if contact and contact[0].lower() == nom_recherche.lower():
                    print(f"Contact trouvé : Nom : {contact[0]}, Téléphone : {contact[1]}, Email : {contact[2]}")
                    found = True
                    break

            if not found:
                print("Aucun contact trouvé avec ce nom.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{CSV_FILE}' est introuvable.")

# Supprimer un contact
def delete_contact():
    nom_suppression = input("Entrez le nom du contact à supprimer : ")
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            contacts = list(reader)

        updated_contacts = [contact for contact in contacts if contact and contact[0].lower() != nom_suppression.lower()]

        if len(contacts) == len(updated_contacts):
            print("Aucun contact trouvé avec ce nom.")
        else:
            with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(updated_contacts)
            print("Contact supprimé avec succès !")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{CSV_FILE}' est introuvable.")

# Menu principal
def main():
    initialize_csv()
    while True:
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choix = input("Entrez votre choix : ")
        if choix == "1":
            add_contact()
        elif choix == "2":
            display_contacts()
        elif choix == "3":
            search_contact()
        elif choix == "4":
            delete_contact()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
