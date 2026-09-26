import csv

def get_videogames():
    videogames = []
    n = int(input("How many videogames do you want to enter?: "))

    for game in range(n):
        name = input("Enter the name of the video game: ")
        genre = input("Enter the genre of the video game: ")
        developer = input("Enter the developer of the video game: ")
        classification = input("Enter the classification of the video game: ") 


        videogame = {
            "nombre": name,
            "genero": genre,
            "desarrollador": developer,
            "clasificacion": classification
        }

        videogames.append(videogame)
        
    return videogames

def write_tab_csv(filename, videogames):
    fieldnames = ["nombre", "genero", "desarrollador", "clasificacion"]

    with open(filename, "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()

        for videogame in videogames:
            writer.writerow(videogame)

if __name__ == "__main__":
    videogames = get_videogames()
    write_tab_csv("videogames.csv", videogames)
