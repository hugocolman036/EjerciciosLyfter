def convert_to_integer(values):
    for element in values:
        try:
            number = int(element)
            print(element, "converted to", number)

        except ValueError:
            print("Could not convert element:", element)


def main():
    my_list = ["4", "hello", "10", "5.2"]

    print("Result:")
    convert_to_integer(my_list)


if __name__ == "__main__":
    main()