from actions import register_students, show_students, show_top_students, calculate_overall_average, delete_student, show_failing_students 
from data import load_students, save_students

# Show menu options

def show_menu():
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Register students")
    print("2. Show students")
    print("3. Show top 3 students")
    print("4. Show overall average")
    print("5. Export students to CSV")
    print("6. Import students from CSV")
    print("7. Delete student")
    print("8. Show failing students")
    print("9. Exit")


# Get and validate the selected option

def get_menu_option():
    while True:
        try:
            menu_option = int(input("Enter a number between 1 and 9: "))
        except ValueError:
            print("The option is not valid.")
            continue

        if menu_option < 1 or menu_option > 9:
            print("The option of the menu must be between 1 and 9.")
            continue

        return menu_option

def run_menu():
    students = []

    while True:
        show_menu()
        option = get_menu_option()

        if option == 9:
            break

        elif option == 1:
            register_students(students)

        elif option == 2:
            show_students(students)

        elif option == 3:
            show_top_students(students)

        elif option == 4:
            overall_average = calculate_overall_average(students)
            print(f"Overall average: {overall_average:.2f}")

        elif option == 5:
            if not students:
                print("No students to export.")
            else:
                save_students(students)
                print("Students exported to CSV successfully.")

        elif option == 6:
            imported_students = load_students()

            if imported_students is not None:
                students = imported_students

                if not imported_students:
                    print("The CSV file exists, but it contains no students.")
                else:
                    print("Students imported from CSV successfully.")

        elif option == 7:
            if not students:
                print("No students to delete.")
            else:
                delete_student(students)

        elif option == 8:
            show_failing_students(students)
