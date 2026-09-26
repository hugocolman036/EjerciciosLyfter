products = [
    {"name": "Monitor", "category": "Electronics", "price": 200},
    {"name": "Keyboard", "category": "Electronics", "price": 50},
    {"name": "Chair", "category": "Furniture", "price": 120},
    {"name": "Table", "category": "Furniture", "price": 180},
    {"name": "Mouse", "category": "Electronics", "price": 25},
]

grouped_categories = {}

for product in products:
    category = product["category"]
    name = product["name"]
    price = product["price"]

    if category not in grouped_categories:
        grouped_categories[category] = {"products": [name], "total_price": price}
    else:
        grouped_categories[category]["products"].append(name)
        grouped_categories[category]["total_price"] += price

print(grouped_categories)

# second option 

grouped_categories = {}

for product in products:
    category = product["category"]
    name = product["name"]
    price = product["price"]

    if category not in grouped_categories:
        grouped_categories[category] = {
            "products": [],
            "total_price": 0
        }

    grouped_categories[category]["products"].append(name)
    grouped_categories[category]["total_price"] += price

print(grouped_categories)