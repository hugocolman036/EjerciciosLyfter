import csv

def read_csv(filename):
    videogames = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for videogame in reader:
            videogames.append(videogame)

    return videogames


def print_videogames(videogames):
    for videogame in videogames:
        print(f"Nombre: {videogame[0]}")
        print(f"Genero: {videogame[1]}")
        print(f"Desarrollador: {videogame[2]}")
        print(f"Clasificacion: {videogame[3]}")


if __name__ == "__main__":
    videogames = read_csv("videogames.csv")
    print_videogames(videogames)