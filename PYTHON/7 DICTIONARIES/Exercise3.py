# List with keys to remove
list_of_keys = ['access_level', 'age']

# Dictionary
employee = {
    'name': 'John',
    'email': 'john@ecorp.com',
    'access_level': 5,
    'age': 28
}

# Remove keys using delete function
for key in list_of_keys:
    if key in employee:
        del employee[key]

# Other option using pop

# for key in list_of_keys:
    # employee.pop(key) careful with the values, you can add (keys, none)


# Result
print(employee)