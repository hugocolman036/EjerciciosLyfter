def filter_words(words, n):

    filtered_words = []

    for word in words:

        if len(word) > n:
            filtered_words.append(word)

    return filtered_words


words = [
    "cielo",
    "sol",
    "maravilloso",
    "día"
]

n = int(input("Enter the minimum number of letters: "))

result = filter_words(words, n)

print(result)