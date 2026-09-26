def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    return lines


def join_lines(lines):
    text = ""

    for line in lines:
        text += line.strip() + " "

    text = text.strip()

    return text


def write_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)


if __name__ == "__main__":
    lines = read_file("text.txt")
    text = join_lines(lines)
    write_file("text_on_line.txt", text)