def get_valid_name():
    while True:
        try:
            name = input("Enter your name: ")

            if name.isdigit():
                raise ValueError("The name cannot be a number.")

            return name

        except ValueError as error:
            print(error)


def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            return age

        except ValueError:
            print("Invalid number.")


def show_greeting(name, age):
    print(f"Hello {name}, your age is {age}")


def main():
    name = get_valid_name()
    age = get_valid_age()

    show_greeting(name, age)


if __name__ == "__main__":
    main()