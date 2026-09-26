def count_letters(text):

    upper = 0
    lower = 0

    for letter in text:

        if letter.isupper():
            upper += 1

        elif letter.islower():
            lower += 1

    print(f"There are {upper} upper cases and {lower} lower cases.")


message = "I love Nación Sushi"

count_letters(message)