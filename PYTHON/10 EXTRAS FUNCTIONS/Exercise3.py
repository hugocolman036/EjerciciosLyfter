def count_vowels(text):

    count = 0

    for letter in text:

        if letter in "aeiouAEIOU":
            count += 1

    return count


message = "Hello World"

result = count_vowels(message)

print(result)