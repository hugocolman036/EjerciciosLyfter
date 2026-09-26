import json


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        pokemons = json.load(file)

    return pokemons


def get_pokemon():
    name = input("Enter the name of the Pokemon: ")
    type = input("Enter the type of Pokemon: ")
    level = int(input("Enter the level of the Pokemon: "))
    weight_kg = float(input("Enter the weight of the Pokemon in kg: "))

    shiny_answer = input("Is the Pokemon shiny? (yes/no): ")

    if shiny_answer == "yes":
        is_shiny = True
    else:
        is_shiny = False

    held_item_answer = input("Enter the held item (or none): ")

    if held_item_answer == "none":
        held_item = None
    else:
        held_item = held_item_answer

    skills = []

    for skill_number in range(4):
        skill = input("Enter a skill of the Pokemon: ")
        skills.append(skill)

    hp = int(input("Enter the HP: "))
    attack = int(input("Enter the attack: "))
    defense = int(input("Enter the defense: "))
    sp_attack = int(input("Enter the special attack: "))
    sp_defense = int(input("Enter the special defense: "))
    speed = int(input("Enter the speed: "))

    stats = {
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "sp_attack": sp_attack,
        "sp_defense": sp_defense,
        "speed": speed
    }

    pokemon = {
        "name": name,
        "type": type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }

    return pokemon


def add_pokemon(pokemons, pokemon):
    pokemons.append(pokemon)


def write_json(filename, pokemons):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(pokemons, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    filename = "pokemons.json"

    pokemons = read_json(filename)
    pokemon = get_pokemon()
    add_pokemon(pokemons, pokemon)
    write_json(filename, pokemons)