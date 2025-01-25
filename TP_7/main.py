from conversion import dollars_to_dirhams, meters_to_kilometers

def main():
    # la conversion dollars en dirhams
    dollars = 2000
    dirhams = dollars_to_dirhams(dollars)
    print(f"{dollars} $ = {dirhams} DH.")

    # la conversion mètres en kilomètres
    meters = 2000
    kilometers = meters_to_kilometers(meters)
    print(f"{meters} m = {kilometers} Km.")

if __name__ == "__main__":
    main()
