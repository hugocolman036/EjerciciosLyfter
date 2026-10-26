import csv
from actions import normalize_student_name

# Function to save students to a CSV file

def save_students(students):
    fieldnames = [
        "name",
        "section",
        "Spanish",
        "English",
        "Social Studies",
        "Science"
    ]

    with open("save_students.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            grades = student["grades"]

            row = {
                "name": student["name"],
                "section": student["section"],
                "Spanish": grades["Spanish"],
                "English": grades["English"],
                "Social Studies": grades["Social Studies"],
                "Science": grades["Science"]
            }

            writer.writerow(row)


# Function to load students from the CSV file

def load_students():
    students = []

    try:
        with open("save_students.csv", mode="r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                spanish_grade = int(row["Spanish"])
                english_grade = int(row["English"])
                social_studies_grade = int(row["Social Studies"])
                science_grade = int(row["Science"])

                grades = {
                    "Spanish": spanish_grade,
                    "English": english_grade,
                    "Social Studies": social_studies_grade,
                    "Science": science_grade
                }

                student = {
                    "name": normalize_student_name(row["name"]),
                    "section": row["section"],
                    "grades": grades
                }

                students.append(student)

    except FileNotFoundError:
        print("The CSV file was not found.")
        return None

    return students

