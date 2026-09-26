import json


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        pokemons = json.load(file)
    return pokemons


def calculate_averages(pokemons):
    pokemon_types = {}

    for pokemon in pokemons:
        pokemon_type = pokemon["type"]
        level = pokemon["level"]

        if pokemon_type in pokemon_types:
            pokemon_types[pokemon_type]["total_level"] += level
            pokemon_types[pokemon_type]["count"] += 1
        else:
            pokemon_types[pokemon_type] = {
                "total_level": level,
                "count": 1
            }

    averages = {}

    for pokemon_type, information in pokemon_types.items():
        average = information["total_level"] / information["count"]
        averages[pokemon_type] = average

    return averages


def show_averages(averages):
    for pokemon_type, average in averages.items():
        print(f"Type: {pokemon_type} → Average level: {average}")


if __name__ == "__main__":
    filename = "/Users/hugocolman/Desktop/PROGRAMACION/FASE 1/UNIDAD 3 PYTHON VSCODE/HOMEWORK 16 JSON/EJERCICIO2/pokemons.json"

    pokemons = read_json(filename)
    averages = calculate_averages(pokemons)
    show_averages(averages)