# Function to get the number of students to add

def get_students_count():

    while True:
        try:
            students_count = int(input("How many students do you want to add?: \n"))

        except ValueError:
            print("Student_count must be a number.")
            continue

        if students_count <= 0:
            print("The number must be bigger than zero.")
            continue

        return students_count


# Function to get a valid grade for a specific subject

def get_valid_grade(subject):
    while True:
        try:
            grade = int(input(f"Enter {subject} grade: "))

        except ValueError:
            print("Grade must be a number.")
            continue

        if grade < 0 or grade > 100:
            print("The number must be between 0 and 100.")
            continue

        return grade


# Function to get all grades for a student

def get_student_grades():
    spanish_grade = get_valid_grade("Spanish")
    english_grade = get_valid_grade("English")
    social_studies_grade = get_valid_grade("Social Studies")
    science_grade = get_valid_grade("Science")

    grades = {
        "Spanish": spanish_grade,
        "English": english_grade,
        "Social Studies": social_studies_grade,
        "Science": science_grade
    }

    return grades


# Function to normalize a student's name by removing extra spaces and capitalizing the first letter of each word

def normalize_student_name(name):
    name = " ".join(name.split())
    name = name.title()
    return name


# Function to get a student's full name

def get_student_name():
    while True:
        name = input("Enter full name of the student: ").strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        name = normalize_student_name(name)
        return name


# Check if student already exists

def student_exists(name, section, students):
    for student in students:
        if student["name"].casefold() == name.casefold() and student["section"].casefold() == section.casefold():
            return True

    return False

# Function to get a student's section

def get_student_section():
    while True:
        section = input("Enter section of the student: ").strip().upper()

        if section == "":
            print("Section cannot be empty.")
            continue

        if len(section) < 2 or len(section) > 3:
            print("Section must have 2 or 3 characters.")
            continue

        if not section[:-1].isdigit() or not section[-1].isalpha():
            print("Section must contain one or two digits followed by a letter.")
            continue

        return section


# Register students and add them to the existing list

def register_students(students):
    students_count = get_students_count()
    registered_count = 0

    while registered_count < students_count:
        student_name = get_student_name()
        student_section = get_student_section()

        if student_exists(student_name, student_section, students):
            print("The student is already registered.")
            continue

        student_grades = get_student_grades()

        student = {}
        student["name"] = student_name
        student["section"] = student_section
        student["grades"] = student_grades

        students.append(student)
        registered_count += 1


# Function to display the information of all registered students

def show_students(students):
    if not students:
        print("No students registered.")
        return

    for student in students:
        print(f'Name: {student["name"]}')
        print(f'Section: {student["section"]}')

        grades = student["grades"]

        for subject, grade in grades.items():
            print(f'{subject}: {grade}')

        print()


# Function to calculate the average grade of a student

def calculate_student_average(grades):
    average = sum(grades.values()) / len(grades)
    return average


# Function to calculate the overall average grade of all students

def calculate_overall_average(students):
    if not students:
        return 0

    total_average = 0

    for student in students:
        student_average = calculate_student_average(student["grades"])
        total_average += student_average

    total_students = len(students)
    overall_average = total_average / total_students

    return overall_average


# Function to get the top 3 students based on their average grades

def get_top_students(students):
    if not students:
        return []

    sorted_students = sorted(
        students,
        key=lambda student: calculate_student_average(student["grades"]),
        reverse=True
    )

    return sorted_students[:3]

# Function to display the top 3 students based on their average grades

def show_top_students(students):
    top_students = get_top_students(students)

    if not top_students:
        print("No students registered.")
        return

    for student in top_students:
        print(f'Name: {student["name"]}')
        print(f'Section: {student["section"]}')
        average = calculate_student_average(student["grades"])
        print(f"Average: {average:.2f}")
        print()


# Delete a student by name and section

def delete_student(students):
    student_name = get_student_name()
    student_section = get_student_section()

    for student in students:
        if student["name"].casefold() == student_name.casefold() and student["section"].casefold() == student_section.casefold():
            confirmation = input("Are you sure you want to delete this student? (yes/no): ")

            if confirmation.lower() == "yes":
                students.remove(student)
                print("Student deleted successfully.")
                return
            else:
                print("Student deletion cancelled.")
                return

    print("Student not found.")


# Get the subjects with failing grades

def get_failing_subjects(grades):
    failing_subjects = []

    for subject, grade in grades.items():
        if grade < 60:
            failing_subjects.append((subject, grade))

    return failing_subjects


# Display students with failing grades

def show_failing_students(students):
    if not students:
        print("No students registered.")
        return

    found_failing_student = False

    for student in students:
        failing_subjects = get_failing_subjects(student["grades"])

        if failing_subjects:
            found_failing_student = True

            print(f'Name: {student["name"]}')
            print(f'Section: {student["section"]}')
            print("Failing subjects:")

            for subject, grade in failing_subjects:
                print(f'{subject}: {grade}')

            print()

    if not found_failing_student:
        print("No failing students found.")