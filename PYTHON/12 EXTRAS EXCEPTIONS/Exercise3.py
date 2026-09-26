def sum_values(values):
    total = 0.0

    for element in values:
        try:
            number = float(element)
            total += number
            print(number, "added successfully")

        except (ValueError, TypeError):
            print("Invalid element:", element)

    return total


def show_total(total):
    print("Total sum:", total)


def main():
    my_list = ["10", "apple", "5.5", "3", "n/a"]

    total = sum_values(my_list)
    show_total(total)


if __name__ == "__main__":
    main()