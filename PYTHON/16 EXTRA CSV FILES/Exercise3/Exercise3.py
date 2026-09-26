import csv


def read_csv(filename):
    videogames = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for videogame in reader:
            videogames.append(videogame)

    return videogames


def count_genres(videogames):
    genres = {}

    for videogame in videogames:
        genre = videogame[1]

        if genre in genres:
            genres[genre] += 1
        else:
            genres[genre] = 1

    return genres


def print_genres(genres):
    print("Géneros encontrados:")

    for genre, count in genres.items():
        print(f"{genre}: {count}")


if __name__ == "__main__":
    videogames = read_csv("videogames.csv")
    genres = count_genres(videogames)
    print_genres(genres)