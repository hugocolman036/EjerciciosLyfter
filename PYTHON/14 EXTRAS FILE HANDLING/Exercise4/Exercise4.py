def get_text():
    text = input("Enter a line of text: ")

    return text


def add_text(filename, text):
    with open(filename, "a") as file:
        file.write(text + "\n")


if __name__ == "__main__":
    text = get_text()
    add_text("records.txt", text)