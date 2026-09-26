my_string = "Pizza con piña"

for index in range(len(my_string) - 1, -1, -1):
    print(my_string[index])

for i in range(13, -1, -1):
    print(my_string[i])

print(my_string[::-1])

for char in reversed(my_string):
    print(char)