with open("exemple.txt","r") as fichier:
    ligne=fichier.readline()
    i=1;
    while ligne:
        print(i,"-",ligne.strip())
        i+=1;
        ligne=fichier.readline()
