import json
from pathlib import Path

def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        pokemons = json.load(file)

    return pokemons


def show_pokemons(pokemons):
    for pokemon in pokemons:
        print(pokemon["name"], pokemon["type"], pokemon["level"])


if __name__ == "__main__":
    filename = Path(__file__).resolve().parent.parent / "17 JSON" / "Exercise2" / "pokemons.json"
    pokemons = read_json(filename)
    show_pokemons(pokemons)