def count_character(text, character):

    count = 0

    for letter in text:
        if letter == character:
            count += 1

    return count


message = "programming"

search = input("Enter the character to search: ")

result = count_character(message, search)

print(f"The character {search} was found {result} times.")