import csv

def read_csv(filename):
    videogames = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for videogame in reader:
            videogames.append(videogame)

    return videogames


def get_developer():
    developer = input("Enter the developer of the videogame: ")
    return developer


def filter_videogames(videogames, developer):
    filtered_videogames = []

    for videogame in videogames:
        if developer == videogame[2]:
            filtered_videogames.append(videogame)

    return filtered_videogames


def print_videogames(videogames, developer):
    print(f"Videojuegos desarrollados por {developer}:")

    for videogame in videogames:
        print(f"- {videogame[0]} (Clasificacion: {videogame[3]}, Genero: {videogame[1]})")


if __name__ == "__main__":
    videogames = read_csv("videogames.csv")
    developer = get_developer()
    filtered_videogames = filter_videogames(videogames, developer)
    print_videogames(filtered_videogames, developer)