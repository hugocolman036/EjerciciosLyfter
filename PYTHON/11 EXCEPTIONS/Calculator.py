def add(current_number, number):
    return current_number + number


def subtract(current_number, number):
    return current_number - number


def multiply(current_number, number):
    return current_number * number


def divide(current_number, number):
    return current_number / number


def show_menu(current_number):
    print()
    print("---------------------------")
    print("Current number:", current_number)
    print("---------------------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")


def get_number():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def main():
    current_number = 0

    while True:
        show_menu(current_number)

        option = input("Choose an option: ")

        match option:
            case "1":
                number = get_number()
                current_number = add(current_number, number)

            case "2":
                number = get_number()
                current_number = subtract(current_number, number)

            case "3":
                number = get_number()
                current_number = multiply(current_number, number)

            case "4":
                number = get_number()

                if number == 0:
                    print("You cannot divide by zero.")
                    continue

                current_number = divide(current_number, number)

            case "5":
                current_number = 0
                print("Result has been cleared.")

            case "6":
                print("Goodbye!")
                break

            case _:
                print("Invalid option.")
                continue

        print("New current number:", current_number)


if __name__ == "__main__":
    main()