downtown_hotel = {
    "name": "marriot",
    "number_of_stars": 5,
    "rooms": [
        {"number": 1, "floor": 0, "price_per_night": 250},
        {"number": 2, "floor": 0, "price_per_night": 250},
        {"number": 3, "floor": 1, "price_per_night": 275},
        {"number": 4, "floor": 1, "price_per_night": 275},
        {"number": 5, "floor": 2, "price_per_night": 300},
        {"number": 6, "floor": 2, "price_per_night": 300},
        {"number": 7, "floor": 3, "price_per_night": 325},
        {"number": 8, "floor": 3, "price_per_night": 325},
        {"number": 9, "floor": 4, "price_per_night": 350},
        {"number": 10, "floor": 4, "price_per_night": 350},
        {"number": 11, "floor": 5, "price_per_night": 400},
        {"number": 12, "floor": 5, "price_per_night": 400},
    ]
}

print(downtown_hotel["name"])

room_4_price = None

for room in downtown_hotel["rooms"]: 
    if room["number"] == 4:
        room_4_price = room["price_per_night"]

print(room_4_price)