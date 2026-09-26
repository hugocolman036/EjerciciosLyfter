import json


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        pokemons = json.load(file)

    return pokemons


def show_stats(pokemons):
    for pokemon in pokemons:
        print("Name:", pokemon["name"])
        print("Attack:", pokemon["stats"]["attack"])
        print("Defense:", pokemon["stats"]["defense"])
        print("Speed:", pokemon["stats"]["speed"])
        print()


if __name__ == "__main__":
    filename = "/Users/hugocolman/Desktop/PROGRAMACION/FASE 1/UNIDAD 3 PYTHON VSCODE/HOMEWORK 16 JSON/EJERCICIO2/pokemons.json"

    pokemons = read_json(filename)
    show_stats(pokemons)