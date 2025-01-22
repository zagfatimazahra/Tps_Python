
def convert_to_int(value):
    try:
        result = int(value)
        print(result)
    except ValueError:
        print("Erreur : la conversion a échoué.")
    
convert_to_int(4.6)
