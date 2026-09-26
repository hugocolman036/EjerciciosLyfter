words = []
counter = 1

# Ask the user for 5 words
while counter <= 5:
    word = input(f"Enter word {counter}: ")
    words.append(word)

    counter += 1

# Create a new list with words longer than 4 letters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

# Results
print(f"\nOriginal list: {words}")
print(f"Words with more than 4 letters: {long_words}")