import json


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        pokemons = json.load(file)

    return pokemons


def get_type():
    pokemon_type = input(
        "Enter the type of Pokemon you would like to choose: "
    ).strip().lower()

    return pokemon_type


def filter_pokemons(pokemons, pokemon_type):
    filtered_pokemons = []

    for pokemon in pokemons:
        if pokemon["type"].lower() == pokemon_type:
            filtered_pokemons.append(pokemon)

    return filtered_pokemons


def show_pokemons(filtered_pokemons):
    print("The Pokemon that exist of that type are:")

    for pokemon in filtered_pokemons:
        print(pokemon["name"])


if __name__ == "__main__":
    filename = "/Users/hugocolman/Desktop/PROGRAMACION/FASE 1/UNIDAD 3 PYTHON VSCODE/HOMEWORK 16 JSON/EJERCICIO 2/pokemons.json"

    pokemons = read_json(filename)
    pokemon_type = get_type()
    filtered_pokemons = filter_pokemons(pokemons, pokemon_type)
    show_pokemons(filtered_pokemons)