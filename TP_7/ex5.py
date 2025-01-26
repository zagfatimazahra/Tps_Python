import pandas as pd

# Lecture du fichier CSV
file_path = "employes.csv"  # Assurez-vous que ce fichier est dans le même répertoire ou spécifiez le chemin complet
df = pd.read_csv(file_path)

# Afficher les cinq premières lignes
print("Les 5 premières lignes :")
print(df.head())

# Calculs simples
print("\nStatistiques sur les salaires :")
print(f"Salaire moyen : {df['Salaire'].mean():.2f}")
print(f"Salaire minimum : {df['Salaire'].min()}")
print(f"Salaire maximum : {df['Salaire'].max()}")

# Groupement par département
print("\nSalaire moyen par département :")
print(df.groupby('Département')['Salaire'].mean())
