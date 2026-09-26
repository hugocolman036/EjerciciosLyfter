def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    return lines


def uppercase_text(lines):
    uppercase_lines = []

    for line in lines:
        uppercase_lines.append(line.upper())

    return uppercase_lines


def write_file(filename, lines):
    with open(filename, "w") as new_file:
        new_file.writelines(lines)


if __name__ == "__main__":
    lines = read_file("text.txt")
    uppercase_lines = uppercase_text(lines)
    write_file("text_uppercase.txt", uppercase_lines)