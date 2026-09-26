def read_file(filename):
    with open(filename, "r") as file:
        text = file.read()

    return text


def count_words(text):
    words = text.split()
    number_of_words = len(words)

    return number_of_words


if __name__ == "__main__":
    text = read_file("text.txt")
    number_of_words = count_words(text)
    print(f"This file has {number_of_words} words")