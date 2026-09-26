grade_total = int(input("Enter the number of grades: "))
grade_counter = 1

number_passing_grades = 0
number_failing_grades = 0

sum_passing = 0
sum_failing = 0
sum_total = 0

# Condition to determine if a grade is passed or failed and accumulate them into the total sum 
while grade_counter <= grade_total:
    current_grade = float(input("Enter the current grade: "))

    sum_total += current_grade

    if current_grade < 70:
        number_failing_grades += 1
        sum_failing += current_grade
    else:
        number_passing_grades += 1
        sum_passing += current_grade

    grade_counter += 1

# Averages
average_total = sum_total / grade_total

if number_passing_grades > 0:
    average_passing_grades = sum_passing / number_passing_grades
else:
    average_passing_grades = 0

if number_failing_grades > 0:
    average_failing_grades = sum_failing / number_failing_grades
else:
    average_failing_grades = 0

# Results
print(f"The student has {number_passing_grades} passing grades")
print(f"Average of passing grades: {average_passing_grades}")
print(f"The student has {number_failing_grades} failing grades")
print(f"Average of failing grades: {average_failing_grades}")
print(f"Total average: {average_total}")