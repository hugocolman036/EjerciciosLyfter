keys = ['first name', 'last name', 'role']
values = ['Alex', 'Castillo', 'Software Engineer']

dictionary = {}

# Iteration
for i in range(len(keys)):
    key = keys[i]
    value = values[i]
    dictionary[key] = value

print(dictionary)

# Second option

keys = ['first name', 'last name', 'role']
values = ['Alex', 'Castillo', 'Software Engineer']

dictionary = {}

# dictionary = dict(zip(keys, values))

for key, value in zip(keys, values):
    dictionary[key] = value

print(dictionary)