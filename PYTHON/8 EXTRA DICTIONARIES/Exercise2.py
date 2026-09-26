employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

grouped_departments = {}

for employee in employees:

    department = employee["department"]
    name = employee["name"]

    if department not in grouped_departments:
        grouped_departments[department] = [name]
    else:
        grouped_departments[department].append(name)

print(grouped_departments)