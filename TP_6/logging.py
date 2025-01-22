import logging

logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_error(message):
    logging.error(message)

def read_file(file_name):
   
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        log_error(f"Fichier introuvable : {file_name} - {e}")
        print("Erreur : Le fichier est introuvable. Consultez le fichier error.log pour plus de détails.")

if __name__ == "__main__":
    file_content = read_file("fichier_inexistant.txt")