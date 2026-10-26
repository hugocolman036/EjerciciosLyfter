import csv


def read_csv(filename):
    videogames = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for videogame in reader:
            videogames.append(videogame)

    return videogames


def get_classification():
    classification = input("Enter the classification of the videogame: ")
    return classification


def filter_videogames(videogames, classification):
    filtered_classification_list = []

    for videogame in videogames:
        if classification == videogame[3]:
            filtered_classification_list.append(videogame)

    return filtered_classification_list


def print_videogames(videogames):
    for videogame in videogames:
        print(f"Nombre: {videogame[0]}")
        print(f"Genero: {videogame[1]}")
        print(f"Desarrollador: {videogame[2]}")
        print(f"Clasificacion: {videogame[3]}")


if __name__ == "__main__":
    videogames = read_csv("videogames.csv")
    classification = get_classification()
    filtered_videogames = filter_videogames(videogames, classification)
    print_videogames(filtered_videogames)