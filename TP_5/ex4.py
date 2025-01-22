import csv

# Fonction pour créer un fichier CSV
def create_contacts_csv():
    header = ["Nom", "Âge", "Ville"]
    data = [
        {"Nom": "Alice", "Âge": 30, "Ville": "Paris"},
        {"Nom": "Alame", "Âge": 22, "Ville": "Tanger"},
        {"Nom": "Othmani", "Âge": 24, "Ville": "Taza"}
    ]

    with open("contacts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

# Fonction pour lire un fichier CSV et afficher les contacts
def read_contacts_csv():
    """Lit le fichier 'contacts.csv' et affiche les informations de chaque contact dans un format lisible."""
    try:
        with open("contacts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"Nom : {row['Nom']}, Âge : {row['Âge']}, Ville : {row['Ville']}")
    except FileNotFoundError:
        print("Erreur : Le fichier 'contacts.csv' est introuvable.")

if __name__ == "__main__":
    create_contacts_csv()
    read_contacts_csv()    
